"""Support for Devialet Phantom speakers."""
from __future__ import annotations

import asyncio
import datetime
import json

import aiohttp

from .const import LOGGER, NORMAL_INPUTS, SPEAKER_POSITIONS, UrlSuffix


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

    async def async_update(self) -> bool | None:
        """Get the latest details from the device."""
        if self._general_info is None:
            self._general_info = await self.get_request(UrlSuffix.GET_GENERAL_INFO)

        # Without general info the device has not been online yet
        if self._general_info is None:
            return False

        self._source_state = await self.get_request(UrlSuffix.GET_CURRENT_SOURCE)
        # the source state call if enough to find out if the device is available (On or Off)
        if not self._is_available:
            return True

        if self._sources is None:
            self._sources = await self.get_request(UrlSuffix.GET_SOURCES)

        self._volume = await self.get_request(UrlSuffix.GET_VOLUME)
        self._night_mode = await self.get_request(UrlSuffix.GET_NIGHT_MODE)
        self._equalizer = await self.get_request(UrlSuffix.GET_EQUALIZER)

        try:
            self._media_duration = self._source_state["metadata"]["duration"]
        except (KeyError, TypeError):
            self._media_duration = None
            self._current_position = None
            self._position_updated_at = None

        if self._media_duration == 0:
            self._media_duration = None

        if self._media_duration is not None:
            position = await self.get_request(UrlSuffix.GET_CURRENT_POSITION)
            try:
                self._current_position = position["position"]
                self._position_updated_at = datetime.datetime.utcnow()
            except (KeyError, TypeError):
                self._current_position = None
                self._position_updated_at = None

        return True

    @property
    def is_available(self) -> bool | None:
        """Return available."""
        return self._is_available

    @property
    def device_id(self) -> str | None:
        """Return the device id."""
        try:
            return self._general_info["deviceId"]
        except (KeyError, TypeError):
            return None

    @property
    def serial(self) -> str | None:
        """Return the serial."""
        try:
            return self._general_info["serial"]
        except (KeyError, TypeError):
            return None

    @property
    def device_name(self) -> str | None:
        """Return the device name."""
        try:
            return self._general_info["deviceName"]
        except (KeyError, TypeError):
            return None

    @property
    def device_role(self) -> str | None:
        """Return the device role."""
        try:
            return self._general_info["role"]
        except (KeyError, TypeError):
            return None

    @property
    def model(self) -> str | None:
        """Return the device model."""
        try:
            return self._general_info["model"]
        except (KeyError, TypeError):
            return None

    @property
    def version(self) -> str | None:
        """Return the device version."""
        try:
            return self._general_info["release"]["version"]
        except (KeyError, TypeError):
            return None

    @property
    def source_state(self) -> any | None:
        """Return the source state object."""
        return self._source_state

    @property
    def playing_state(self) -> str | None:
        """Return the state of the device."""
        try:
            return self._source_state["playingState"]
        except (KeyError, TypeError):
            return None

    @property
    def volume_level(self) -> float | None:
        """Volume level of the media player (0..1)."""
        try:
            return self._volume["volume"] * 0.01
        except (KeyError, TypeError):
            return None

    @property
    def is_volume_muted(self) -> bool | None:
        """Return boolean if volume is currently muted."""
        try:
            return self._source_state["muteState"] == "muted"
        except (KeyError, TypeError):
            return None

    @property
    def source_list(self) -> list | None:
        """Return the list of available input sources."""

        if self._sources is None or len(self._source_list) > 0:
            return sorted(self._source_list)

        for source in self._sources["sources"]:
            source_type = source["type"]
            device_id = source["deviceId"]

            if self.device_role in SPEAKER_POSITIONS and source_type in (
                "optical",
                "opticaljack",
            ):
                # Stereo devices have the role FrontLeft or FrontRight.
                # Add a suffix to the source to recognize the device.
                for role, position in SPEAKER_POSITIONS.items():
                    if (device_id == self.device_id and role == self.device_role) or (
                        device_id != self.device_id and role != self.device_role
                    ):
                        source_type = source_type + "_" + position

            for pretty_name, name in NORMAL_INPUTS.items():
                if name == source_type:
                    self._source_list[pretty_name] = name

        return sorted(self._source_list)

    @property
    def available_options(self) -> any | None:
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
    def media_title(self) -> str | None:
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
    def supported_features(self) -> any | None:
        """Flag media player features that are supported."""
        try:
            return self._source_state["availableOptions"]
        except (KeyError, TypeError):
            return None

    @property
    def source(self) -> str | None:
        """Return the current input source."""
        try:
            source_id = self._source_state["source"]["sourceId"]
            device_id = self._source_state["source"]["deviceId"]

            # Devialet Arch has a different source description.
            for source in self._sources["sources"]:
                if source["sourceId"] == source_id and source["deviceId"] == device_id:
                    source_type = source["type"]

                    if (
                        source_type == "optical" or source_type == "opticaljack"
                    ) and self.device_role in SPEAKER_POSITIONS:
                        for role, position in SPEAKER_POSITIONS.items():
                            if (
                                device_id == self.device_id and role == self.device_role
                            ) or (
                                device_id != self.device_id and role != self.device_role
                            ):
                                source_type = source_type + "_" + position
                    return source_type
        except (KeyError, TypeError):
            return None
        return None

    @property
    def night_mode(self) -> bool | None:
        """Return the current nightmode state."""
        try:
            return self._night_mode["nightMode"] == "on"
        except (KeyError, TypeError):
            return None

    @property
    def equalizer(self) -> str | None:
        """Return the current equalizer preset."""
        try:
            if self._equalizer["enabled"]:
                return self._equalizer["preset"]
        except (KeyError, TypeError):
            return None

    async def async_get_diagnostics(self) -> any | None:
        """Return the diagnostic data."""
        return {
            "is_available": self._is_available,
            "general_info": self._general_info,
            "sources": self._sources,
            "source_state": self._source_state,
            "volume": self._volume,
            "night_mode": self._night_mode,
            "equalizer": self._equalizer,
            "source_list": self.source_list,
            "source": self.source,
        }

    async def async_volume_up(self) -> None:
        """Volume up media player."""
        await self.post_request(UrlSuffix.VOLUME_UP, {})

    async def async_volume_down(self) -> None:
        """Volume down media player."""
        await self.post_request(UrlSuffix.VOLUME_DOWN, {})

    async def async_set_volume_level(self, volume: float) -> None:
        """Set volume level, range 0..1."""
        await self.post_request(
            UrlSuffix.VOLUME_SET,
            {"volume": volume * 100},
        )

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute (true) or unmute (false) media player."""
        if mute:
            await self.post_request(UrlSuffix.MUTE, {})
        else:
            await self.post_request(UrlSuffix.UNMUTE, {})

    async def async_media_play(self) -> None:
        """Play media player."""
        await self.post_request(UrlSuffix.PLAY, {})

    async def async_media_pause(self) -> None:
        """Pause media player."""
        await self.post_request(UrlSuffix.PAUSE, {})

    async def async_media_stop(self) -> None:
        """Pause media player."""
        await self.post_request(UrlSuffix.PAUSE, {})

    async def async_media_next_track(self) -> None:
        """Send the next track command."""
        await self.post_request(UrlSuffix.NEXT_TRACK, {})

    async def async_media_previous_track(self) -> None:
        """Send the previous track command."""
        await self.post_request(UrlSuffix.PREVIOUS_TRACK, {})

    async def async_media_seek(self, position: float) -> None:
        """Send seek command."""

        await self.post_request(
            UrlSuffix.SEEK,
            {"position": int(position)},
        )

    async def async_set_night_mode(self, night_mode: bool) -> None:
        """Set the night mode."""
        if night_mode:
            mode = "on"
        else:
            mode = "off"

        await self.post_request(
            UrlSuffix.NIGHT_MODE,
            {"nightMode": mode},
        )

    async def async_set_equalizer(self, preset: str) -> None:
        """Set the equalizer preset."""
        await self.post_request(
            UrlSuffix.EQUALIZER,
            {"preset": preset},
        )

    async def async_turn_off(self) -> None:
        """Turn off media player."""
        await self.post_request(UrlSuffix.TURN_OFF, {})

    async def async_select_source(self, source: str) -> None:
        """Select input source."""
        source_id = None

        try:
            name = NORMAL_INPUTS[source]
        except KeyError:
            LOGGER.error("Unknown source %s selected", source)
            return

        if "_" in name:
            name_split = name.split("_")

            for role, position in SPEAKER_POSITIONS.items():
                if position != name_split[1]:
                    continue

                if role == self.device_role:
                    for _source in self._sources["sources"]:
                        if (
                            _source["deviceId"] == self.device_id
                            and _source["type"] == name_split[0]
                        ):
                            source_id = _source["sourceId"]
                            break
                else:
                    for _source in self._sources["sources"]:
                        if (
                            _source["deviceId"] != self.device_id
                            and _source["type"] == name_split[0]
                        ):
                            source_id = _source["sourceId"]
                            break
                break
        else:
            for _source in self._sources["sources"]:
                if _source["type"] == name:
                    source_id = _source["sourceId"]

        if source_id is None:
            LOGGER.error("Source %s is not available", source)
            return

        await self.post_request(
            str(UrlSuffix.SELECT_SOURCE).replace("%SOURCE_ID%", source_id), {}
        )

    async def get_request(self, suffix=str) -> any | None:
        """Generic GET method."""
        url = "http://" + self._host + str(suffix)

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

    async def post_request(self, suffix=str, body=str) -> any | None:
        """Generic POST method."""
        url = "http://" + self._host + str(suffix)

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
