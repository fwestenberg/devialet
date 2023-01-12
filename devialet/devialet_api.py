"""Support for Devialet Phantom speakers."""
from __future__ import annotations

import json
import logging

import asyncio
import aiohttp
import datetime

from .const import LOGGER, NORMAL_INPUTS, SPEAKER_POSITIONS


class DevialetApi:
    """Devialet API class."""

    def __init__(self, host, session):
        """Initialize the Devialet API."""

        self._host = host
        self._session = session

        self._general_info = None
        self._volume = None
        self._muted = False
        self._source_state = None
        self._current_position = 0
        self._sources = None
        self._night_mode = None
        self._equalizer = None
        self._source_list = {}
        self._position_updated_at = 0
        self._media_duration = 0
        self._device_role = ""
        self._is_available = False

    async def async_update(self):
        """Get the latest details from the device."""

        if self._general_info is None:
            self._general_info = await self.get_request("/ipcontrol/v1/devices/current")

        if self._general_info is None:
            return False

        if self._sources is None:
            self._sources = await self.get_request(
                "/ipcontrol/v1/groups/current/sources"
            )

        self._source_state = await self.get_request(
            "/ipcontrol/v1/groups/current/sources/current"
        )

        if self._source_state is None:
            return self._is_available

        self._volume = await self.get_request(
            "/ipcontrol/v1/systems/current/sources/current/soundControl/volume"
        )

        self._night_mode = await self.get_request(
            "/ipcontrol/v1/systems/current/settings/audio/nightMode",
        )

        self._equalizer = await self.get_request(
            "/ipcontrol/v1/systems/current/settings/audio/equalizer",
        )

        try:
            self._media_duration = self._source_state["metadata"]["duration"]
        except (KeyError, TypeError):
            self._media_duration = None
            self._current_position = None
            self._position_updated_at = None

        if self._media_duration == 0:
            self._media_duration = None

        if self._media_duration is not None:
            position = await self.get_request(
                "/ipcontrol/v1/groups/current/sources/current/playback/position"
            )
            try:
                self._current_position = position["position"]
                self._position_updated_at = datetime.datetime.now()
            except (KeyError, TypeError):
                self._current_position = None
                self._position_updated_at = None

        return True

    @property
    def is_available(self):
        """Return available."""
        return self._is_available

    @property
    def device_id(self):
        """Return the device id."""
        try:
            return self._general_info["deviceId"]
        except (KeyError, TypeError):
            return None

    @property
    def serial(self):
        """Return the serial."""
        try:
            return self._general_info["serial"]
        except (KeyError, TypeError):
            return None

    @property
    def device_name(self):
        """Return the device name."""
        try:
            return self._general_info["deviceName"]
        except (KeyError, TypeError):
            return None

    @property
    def device_role(self):
        """Return the device role."""
        try:
            return self._general_info["role"]
        except (KeyError, TypeError):
            return None

    @property
    def model(self):
        """Return the device model."""
        try:
            return self._general_info["model"]
        except (KeyError, TypeError):
            return None

    @property
    def version(self):
        """Return the device version."""
        try:
            return self._general_info["release"]["version"]
        except (KeyError, TypeError):
            return None

    @property
    def source_state(self):
        """Return the general info."""
        return self._source_state

    @property
    def playing_state(self):
        """Return the state of the device."""
        try:
            return self._source_state["playingState"]
        except (KeyError, TypeError):
            return None

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        try:
            return self._volume["volume"] * 0.01
        except (KeyError, TypeError):
            return None

    @property
    def is_volume_muted(self):
        """Return boolean if volume is currently muted."""
        try:
            return self._source_state["muteState"] == "muted"
        except (KeyError, TypeError):
            return None

    @property
    def source_list(self):
        """Return the list of available input sources."""

        if self._sources is None or len(self._source_list) > 0:
            return sorted(self._source_list)

        for source in self._sources["sources"]:
            source_type = source["type"]
            device_id = source["deviceId"]

            if source_type == "optical":
                position = ""

                if self.device_role in SPEAKER_POSITIONS:
                    for role, position in SPEAKER_POSITIONS.items():
                        if (
                            device_id == self.device_id and role == self.device_role
                        ) or (device_id != self.device_id and role != self.device_role):
                            source_type = source_type + "_" + position

            for pretty_name, name in NORMAL_INPUTS.items():
                if name == source_type:
                    self._source_list[pretty_name] = name

        return sorted(self._source_list)

    @property
    def available_options(self):
        """Return the list of available options for this source."""
        try:
            return self._source_state["availableOptions"]
        except (KeyError, TypeError):
            return None

    @property
    def media_artist(self) -> str | None:
        """Artist of current playing media, music track only."""
        try:
            return self._source_state["metadata"]["artist"]
        except (KeyError, TypeError):
            return None

    @property
    def media_album_name(self) -> str | None:
        """Album name of current playing media, music track only."""
        try:
            return self._source_state["metadata"]["album"]
        except (KeyError, TypeError):
            return None

    @property
    def media_title(self):
        """Return the current media info."""
        try:
            return self._source_state["metadata"]["title"]
        except (KeyError, TypeError):
            return None

    @property
    def media_image_url(self) -> str | None:
        """Image url of current playing media, not available for Airplay."""
        try:
            return self._source_state["metadata"]["coverArtUrl"]
        except (KeyError, TypeError):
            return None

    @property
    def media_duration(self) -> int | None:
        """Duration of current playing media in seconds."""
        return self._media_duration

    @property
    def current_position(self) -> int | None:
        """Position of current playing media in seconds."""
        return self._current_position

    @property
    def position_updated_at(self) -> datetime.datetime | None:
        """When was the position of the current playing media valid."""
        return self._position_updated_at

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        try:
            return self._source_state["availableOptions"]
        except (KeyError, TypeError):
            return None

    @property
    def source(self):
        """Return the current input source."""
        try:
            source_type = self._source_state["source"]["type"]
            device_id = self._source_state["source"]["deviceId"]
        except (KeyError, TypeError):
            return None

        position = ""
        if source_type == "optical" and self.device_role in SPEAKER_POSITIONS:
            for role, position in SPEAKER_POSITIONS.items():
                if (device_id == self.device_id and role == self.device_role) or (
                    device_id != self.device_id and role != self.device_role
                ):
                    source_type = source_type + "_" + position

        return source_type

    @property
    def night_mode(self):
        """Return the current nightmode state."""
        try:
            return self._night_mode["nightMode"] == "on"
        except (KeyError, TypeError):
            return None

    @property
    def equalizer(self):
        """Return the current equalizer preset."""
        try:
            if self._equalizer["enabled"]:
                return self._equalizer["preset"]
        except (KeyError, TypeError):
            return None

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
                "/ipcontrol/v1/groups/current/sources/current/playback/mute", {}
            )
        else:
            await self.post_request(
                "/ipcontrol/v1/groups/current/sources/current/playback/unmute", {}
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

    async def async_set_night_mode(self, night_mode: bool) -> None:
        """Set the night mode."""
        if night_mode:
            mode = "on"
        else:
            mode = "off"

        await self.post_request(
            "/ipcontrol/v1/systems/current/settings/audio/nightMode",
            {"nightMode": mode},
        )

    async def async_set_equalizer(self, preset: str) -> None:
        """Set the equalizer preset."""

        await self.post_request(
            "/ipcontrol/v1/systems/current/settings/audio/equalizer",
            {"preset": preset},
        )

    async def async_turn_off(self) -> None:
        """Turn off media player."""
        await self.post_request("/ipcontrol/v1/systems/current/powerOff", {})

    async def async_select_source(self, source: str) -> None:
        """Select input source."""
        # Not available yet

    async def get_request(self, suffix=str):
        """Generic GET method."""

        url = "http://" + self._host + suffix

        try:
            async with self._session.get(
                url=url, allow_redirects=False, timeout=2
            ) as response:
                response = await response.read()
                LOGGER.debug(
                    "Host %s: HTTP Response data: %s",
                    self._host,
                    response,
                )

            response_json = json.loads(response)
            self._is_available = True

            if "error" in response_json:
                LOGGER.debug(response_json["error"])
                return None

            return response_json

        except aiohttp.ClientConnectorError as conn_err:
            LOGGER.debug("Host %s: Connection error %s", self._host, str(conn_err))
            self._is_available = False
            return None
        except asyncio.TimeoutError:
            self._is_available = False
            LOGGER.debug(
                "Devialet connection timeout exception. Please check the connection"
            )
            return None
        except (TypeError, json.JSONDecodeError):
            LOGGER.debug("Devialet: JSON error")
            return None
        except Exception:  # pylint: disable=bare-except
            LOGGER.debug("Devialet: unknown exception occurred")
            return None

    async def post_request(self, suffix=str, body=str):
        """Generic POST method."""

        url = "http://" + self._host + suffix

        try:
            async with self._session.post(
                url=url, json=body, allow_redirects=False, timeout=2
            ) as response:
                response = await response.read()
                LOGGER.debug(
                    "Host %s: HTTP Response data: %s",
                    self._host,
                    response,
                )

            return True

        except aiohttp.ClientConnectorError as conn_err:
            LOGGER.debug("Host %s: Connection error %s", self._host, str(conn_err))
            return False
        except asyncio.TimeoutError:
            LOGGER.debug(
                "Devialet connection timeout exception. Please check the connection"
            )
            return False
        except (TypeError, json.JSONDecodeError):
            LOGGER.debug("Devialet: JSON error")
            return False
        except Exception:  # pylint: disable=bare-except
            LOGGER.debug("Devialet: unknown exception occurred")
            return False
