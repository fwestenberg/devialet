"""Support for Devialet Phantom speakers."""
from __future__ import annotations
from datetime import timedelta

import json
import logging

import asyncio
import aiohttp
import datetime

from homeassistant.components.media_player import (
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.const import CONF_IP_ADDRESS, CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.config_entries import ConfigEntry

from homeassistant.components.persistent_notification import DOMAIN as PN_DOMAIN

from .const import DOMAIN, DEFAULT_NAME, DEFAULT_SCAN_INTERVAL

SCAN_INTERVAL = timedelta(seconds=DEFAULT_SCAN_INTERVAL)

_LOGGER = logging.getLogger(__name__)

SUPPORT_DEVIALET = (
    MediaPlayerEntityFeature.VOLUME_SET
    | MediaPlayerEntityFeature.VOLUME_MUTE
    | MediaPlayerEntityFeature.TURN_ON
    | MediaPlayerEntityFeature.TURN_OFF
    | MediaPlayerEntityFeature.SELECT_SOURCE
    | MediaPlayerEntityFeature.SELECT_SOUND_MODE
)

SUPPORT_MEDIA_MODES = (
    MediaPlayerEntityFeature.PAUSE
    | MediaPlayerEntityFeature.STOP
    | MediaPlayerEntityFeature.PREVIOUS_TRACK
    | MediaPlayerEntityFeature.NEXT_TRACK
    | MediaPlayerEntityFeature.PLAY
    | MediaPlayerEntityFeature.SEEK
)

NORMAL_INPUTS = {
    "Phono": "phono",
    "Line": "line",
    "Digital left": "digital_left",
    "Digital right": "digital_right",
    "Optical": "optical",
    "Optical jack": "opticaljack",
    "Spotify Connect": "spotifyconnect",
    "Airplay": "airplay2",
    "Bluetooth": "bluetooth",
    "Online": "upnp",
    "Raat": "raat",
}

SOUND_MODES = {
    "Normal": "normal",
    "Night mode": "night mode",
}


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the Devialet entry."""
    session = async_get_clientsession(hass)

    async_add_entities(
        [DevialetDevice(entry.data[CONF_IP_ADDRESS], session)],
        update_before_add=True,
    )


class DevialetDevice(MediaPlayerEntity):
    """Representation of a Devialet device."""

    def __init__(self, host, session):
        """Initialize the Devialet device."""
        # SCAN_INTERVAL = timedelta(seconds=scan_interval)

        self._name = DEFAULT_NAME
        self._host = host

        self._general_info = None
        self._volume = None
        self._muted = False
        self._sourcestate = None
        self._currentposition = 0
        self._sources = None
        self._session = session
        self._available = False
        self._source_list = {}
        self._position_updated_at = 0
        self._media_duration = 0

    async def async_update(self):
        """Get the latest details from the device."""

        if self._general_info is None:
            self._general_info = await self.get_request("/ipcontrol/v1/devices/current")
        if self._general_info is None:
            return False

        self._volume = await self.get_request(
            "/ipcontrol/v1/systems/current/sources/current/soundControl/volume"
        )
        if self._volume is None:
            return True

        self._sourcestate = await self.get_request(
            "/ipcontrol/v1/groups/current/sources/current"
        )

        if self._sources is None:
            self._sources = await self.get_request(
                "/ipcontrol/v1/groups/current/sources"
            )

        try:
            self._media_duration = self._sourcestate["metadata"]["duration"]
        except KeyError:
            self._media_duration = 0
            self._currentposition = None
            self._position_updated_at = None

        if self._media_duration > 0:
            position = await self.get_request(
                "/ipcontrol/v1/groups/current/sources/current/playback/position"
            )
            try:
                self._currentposition = position["position"]
                self._position_updated_at = datetime.datetime.now()
            except KeyError:
                self._currentposition = None
                self._position_updated_at = None

        return True

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        _LOGGER.info(self._general_info)
        if not self._general_info:
            return None

        try:
            return DeviceInfo(
                identifiers={
                    # Serial numbers are unique identifiers within a specific domain
                    (DOMAIN, self._general_info["deviceId"])
                },
                name=self._name,
                manufacturer="Devialet",
                model=self._general_info["model"],
                sw_version=self._general_info["release"]["version"],
            )
        except KeyError:
            return None

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def unique_id(self):
        """Return the name of the device."""
        if not self._general_info:
            return None

        return self._general_info["deviceId"]

    @property
    def state(self) -> MediaPlayerState | None:
        """Return the state of the device."""
        if not self._sourcestate:
            return None

        try:
            playingstate = self._sourcestate["playingState"]
        except KeyError:
            return None

        if not self._available:
            return MediaPlayerState.OFF
        if self._volume is None:
            return MediaPlayerState.IDLE
        if playingstate == "playing":
            return MediaPlayerState.PLAYING
        elif playingstate == "paused":
            return MediaPlayerState.PAUSED
        else:
            return MediaPlayerState.ON

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        if not self._volume:
            return None

        try:
            return self._volume["volume"] * 0.01
        except KeyError:
            return None

    @property
    def is_volume_muted(self):
        """Return boolean if volume is currently muted."""
        if not self._sourcestate:
            return None

        try:
            return self._sourcestate["muteState"] == "muted"
        except KeyError:
            return None

    @property
    def source_list(self):
        """Return the list of available input sources."""

        if self._sources is None or len(self._source_list) > 0:
            return sorted(self._source_list)

        for source in self._sources["sources"]:
            source_type = source["type"]

            for pretty_name, name in NORMAL_INPUTS.items():
                if name == source_type:
                    self._source_list[pretty_name] = name

        return sorted(self._source_list)

    @property
    def sound_mode_list(self):
        """Return the list of available sound modes."""
        return sorted(SOUND_MODES)

    @property
    def media_artist(self) -> str | None:
        """Artist of current playing media, music track only."""
        if not self._sourcestate:
            return None

        try:
            return self._sourcestate["metadata"]["artist"]
        except KeyError:
            return None

    @property
    def media_album_name(self) -> str | None:
        """Album name of current playing media, music track only."""
        if not self._sourcestate:
            return None

        try:
            return self._sourcestate["metadata"]["album"]
        except KeyError:
            return None

    @property
    def media_title(self):
        """Return the current media info."""
        if not self._sourcestate:
            return None

        try:
            return self._sourcestate["metadata"]["title"]
        except KeyError:
            return None

    @property
    def media_image_url(self) -> str | None:
        """Image url of current playing media."""
        if not self._sourcestate:
            return None

        try:
            return self._sourcestate["metadata"]["coverArtUrl"]
        except KeyError:
            return None

    @property
    def media_duration(self) -> int | None:
        """Duration of current playing media in seconds."""
        return self._media_duration

    @property
    def media_position(self) -> int | None:
        """Position of current playing media in seconds."""
        return self._currentposition

    @property
    def media_position_updated_at(self) -> datetime.datetime | None:
        """When was the position of the current playing media valid."""
        return self._position_updated_at

    @property
    def supported_features(self) -> MediaPlayerEntityFeature:
        """Flag media player features that are supported."""
        features = SUPPORT_DEVIALET

        if self._sourcestate is None:
            return features

        available_options = self._sourcestate["availableOptions"]

        if "play" in available_options:
            features = features | MediaPlayerEntityFeature.PLAY
        if "pause" in available_options:
            features = (
                features
                | MediaPlayerEntityFeature.PAUSE
                | MediaPlayerEntityFeature.STOP
            )
        if "previous" in available_options:
            features = features | MediaPlayerEntityFeature.PREVIOUS_TRACK
        if "next" in available_options:
            features = features | MediaPlayerEntityFeature.NEXT_TRACK
        if "seek" in available_options:
            features = features | MediaPlayerEntityFeature.SEEK
        return features

    @property
    def source(self):
        """Return the current input source."""
        if not self._sourcestate:
            return None

        try:
            source = self._sourcestate["source"]["type"]
        except KeyError:
            return None

        for pretty_name, name in self._source_list.items():
            if source == name:
                return pretty_name

    async def async_volume_up(self) -> None:
        """Volume up media player."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/soundControl/volumeUp", {}
        )

    async def async_volume_down(self) -> None:
        """Volume down media player."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/soundControl/volumeDown", {}
        )

    async def async_set_volume_level(self, volume: float) -> None:
        """Set volume level, range 0..1."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/soundControl/volume",
            {"volume": volume * 100},
        )

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute (true) or unmute (false) media player."""
        if mute:
            await self.post_request(
                "/ipcontrol/v1/systems/current/sources/current/soundControl/mute", {}
            )
        else:
            await self.post_request(
                "/ipcontrol/v1/systems/current/sources/current/soundControl/unmute", {}
            )

    async def async_media_play(self) -> None:
        """Play media player."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/play", {}
        )

    async def async_media_pause(self) -> None:
        """Pause media player."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/pause", {}
        )

    async def async_media_stop(self) -> None:
        """Pause media player."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/pause", {}
        )

    async def async_media_next_track(self) -> None:
        """Send the next track command."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/next", {}
        )

    async def async_media_previous_track(self) -> None:
        """Send the previous track command."""
        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/previous", {}
        )

    async def async_media_seek(self, position: float) -> None:
        """Send seek command."""

        await self.post_request(
            "/ipcontrol/v1/systems/current/sources/current/playback/position",
            {"position": int(position)},
        )

    async def async_select_sound_mode(self, sound_mode: str) -> None:
        if sound_mode == "Normal" or sound_mode is None:
            mode = "off"
        else:
            mode = "on"

        await self.post_request(
            "/ipcontrol/v1/systems/current/settings/audio/nightMode",
            {"nightMode": mode},
        )

    async def async_turn_on(self) -> None:
        """Turn the media player on."""
        await self.hass.services.async_call(
            PN_DOMAIN,
            "create",
            service_data={
                "title": "Devialet turn on",
                "message": "Please use the physical button to turn the device on",
            },
            blocking=False,
        )

    async def async_turn_off(self) -> None:
        """Turn off media player."""
        await self.post_request("/ipcontrol/v1/systems/current/powerOff", {})

    async def async_select_source(self, source: str) -> None:
        """Select input source."""
        # Not available yet?

    async def get_request(self, suffix=str):
        """Generic GET method."""

        url = "http://" + self._host + suffix

        try:
            async with self._session.get(url=url, allow_redirects=False) as response:
                response = await response.read()
                _LOGGER.debug(
                    "%s/%s::send() HTTP Response data: %s",
                    self.name,
                    self._host,
                    response,
                )
            self._available = True
            response_json = json.loads(response)

            if "error" in response_json:
                _LOGGER.debug(response_json["error"])
                return None

            return response_json

        except aiohttp.ClientConnectorError as conn_err:
            _LOGGER.debug("Host %s: Connection error %s", self._host, str(conn_err))
            raise
        except asyncio.TimeoutError:
            _LOGGER.debug(
                "Devialet connection timeout exception. Please check the connection"
            )
            raise
        except (TypeError, json.JSONDecodeError):
            _LOGGER.debug("Devialet: JSON error")
            raise
        except Exception:  # pylint: disable=bare-except
            _LOGGER.debug("Devialet: unknown exception occurred")
            raise

    async def post_request(self, suffix=str, body=str):
        """Generic POST method."""

        url = "http://" + self._host + suffix

        try:
            async with self._session.post(
                url=url, json=body, allow_redirects=False
            ) as response:
                response = await response.read()
                _LOGGER.debug(
                    "%s/%s::send() HTTP Response data: %s",
                    self.name,
                    self._host,
                    response,
                )

            return True

        except aiohttp.ClientConnectorError as conn_err:
            _LOGGER.debug("Host %s: Connection error %s", self._host, str(conn_err))
            raise
        except asyncio.TimeoutError:
            _LOGGER.debug(
                "Devialet connection timeout exception. Please check the connection"
            )
            raise
        except (TypeError, json.JSONDecodeError):
            _LOGGER.debug("Devialet: JSON error")
            raise
        except Exception:  # pylint: disable=bare-except
            _LOGGER.debug("Devialet: unknown exception occurred")
            raise
