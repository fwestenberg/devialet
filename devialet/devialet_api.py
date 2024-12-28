"""Support for Devialet Phantom speakers1."""
from __future__ import annotations

import asyncio
import datetime
import json
import re
from typing import Mapping, Union

import aiohttp
from async_upnp_client.aiohttp import AiohttpRequester
from async_upnp_client.client_factory import UpnpFactory
from async_upnp_client.exceptions import (UpnpActionResponseError,
                                          UpnpXmlParseError)
from async_upnp_client.profiles.dlna import DmrDevice
from async_upnp_client.search import async_search
from async_upnp_client.utils import CaseInsensitiveDict

from .const import AV_TRANSPORT, LOGGER, NORMAL_INPUTS, MEDIA_RENDERER, SPEAKER_POSITIONS, UrlSuffix

UPNP_SEARCH_INTERVAL = 120

class DevialetApi:
    """Devialet API class."""

    def __init__(self, host:str, session:aiohttp.ClientSession):
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
        self._upnp_device = None
        self._dmr_device = None
        self._last_upnp_search: datetime.datetime = None

    async def async_update(self) -> bool | None:
        """Get the latest details from the device."""
        if self._general_info is None:
            self._general_info = await self._async_get_request(UrlSuffix.GET_GENERAL_INFO)

        # Without general info the device has not been online yet
        if self._general_info is None:
            return False

        self._source_state = await self._async_get_request(UrlSuffix.GET_CURRENT_SOURCE)
        # The source state call is enough to find out if the device is available (On or Off)
        if not self._is_available:
            # Set upnp to none, so discovery will find the new port when it's online again
            self._upnp_device = None
            self._dmr_device = None
            return True

        if self._sources is None:
            self._sources = await self._async_get_request(UrlSuffix.GET_SOURCES)

        self._volume = await self._async_get_request(UrlSuffix.GET_VOLUME)
        self._night_mode = await self._async_get_request(UrlSuffix.GET_NIGHT_MODE)
        self._equalizer = await self._async_get_request(UrlSuffix.GET_EQUALIZER)

        try:
            self._media_duration = self._source_state["metadata"]["duration"]
        except (KeyError, TypeError):
            self._media_duration = None
            self._current_position = None
            self._position_updated_at = None

        if self._media_duration == 0:
            self._media_duration = None

        if self._media_duration is not None:
            position = await self._async_get_request(UrlSuffix.GET_CURRENT_POSITION)
            try:
                self._current_position = position["position"]
                self._position_updated_at = datetime.datetime.now(tz=datetime.timezone.utc).replace(tzinfo=None)
            except (KeyError, TypeError):
                self._current_position = None
                self._position_updated_at = None

        return True

    @property
    def is_available(self) -> bool | None:
        """Return available."""
        return self._is_available

    @property
    def upnp_available(self) -> bool | None:
        """Return available."""
        return self._upnp_device is not None

    @property
    def device_id(self) -> str | None:
        """Return the device id."""
        try:
            return self._general_info["deviceId"]
        except (KeyError, TypeError):
            return None

    @property
    def is_system_leader(self) -> bool | None:
        """Return the boolean for system leader identification."""
        try:
            return self._general_info["isSystemLeader"]
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
    def dmr_device(self) -> DmrDevice | None:
        """Return DMR device class."""
        return self._dmr_device

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
    def available_operations(self) -> any | None:
        """Return the list of available operations for this source."""
        try:
            return self._source_state["availableOperations"]
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
            "upnp_device_type": getattr(self._upnp_device.device_info, 'device_type') if self._upnp_device else "Not available",
            "upnp_device_url": getattr(self._upnp_device.device_info, 'url') if self._upnp_device else "Not available",
        }

    async def async_volume_up(self) -> None:
        """Volume up media player."""
        await self._async_post_request(UrlSuffix.VOLUME_UP)

    async def async_volume_down(self) -> None:
        """Volume down media player."""
        await self._async_post_request(UrlSuffix.VOLUME_DOWN)

    async def async_set_volume_level(self, volume: float) -> None:
        """Set volume level, range 0..1."""
        await self._async_post_request(
            UrlSuffix.VOLUME_SET,
            json_body={"volume": volume * 100},
        )

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute (true) or unmute (false) media player."""
        if mute:
            await self._async_post_request(UrlSuffix.MUTE)
        else:
            await self._async_post_request(UrlSuffix.UNMUTE)

    async def async_media_play(self) -> None:
        """Play media player."""
        await self._async_post_request(UrlSuffix.PLAY)

    async def async_media_pause(self) -> None:
        """Pause media player."""
        await self._async_post_request(UrlSuffix.PAUSE)

    async def async_media_stop(self) -> None:
        """Pause media player."""
        await self._async_post_request(UrlSuffix.PAUSE)

    async def async_media_next_track(self) -> None:
        """Send the next track command."""
        await self._async_post_request(UrlSuffix.NEXT_TRACK)

    async def async_media_previous_track(self) -> None:
        """Send the previous track command."""
        await self._async_post_request(UrlSuffix.PREVIOUS_TRACK)

    async def async_media_seek(self, position: float) -> None:
        """Send seek command."""

        await self._async_post_request(
            UrlSuffix.SEEK,
            json_body={"position": int(position)},
        )

    async def async_set_night_mode(self, night_mode: bool) -> None:
        """Set the night mode."""
        if night_mode:
            mode = "on"
        else:
            mode = "off"

        await self._async_post_request(
            UrlSuffix.NIGHT_MODE,
            json_body={"nightMode": mode},
        )

    async def async_set_equalizer(self, preset: str) -> None:
        """Set the equalizer preset."""
        await self._async_post_request(
            UrlSuffix.EQUALIZER,
            json_body={"preset": preset},
        )

    async def async_turn_off(self) -> None:
        """Turn off media player."""
        await self._async_post_request(UrlSuffix.TURN_OFF)

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

        await self._async_post_request(
            str(UrlSuffix.SELECT_SOURCE).replace("%SOURCE_ID%", source_id)
        )

    async def _async_get_request(self, suffix: str) -> any | None:
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
            LOGGER.debug("Devialet connection timeout exception. Please check the connection")
            self._is_available = False
            return None
        except (TypeError, json.JSONDecodeError):
            LOGGER.debug("Get request: JSON error")
            return None
        except Exception:  # pylint: disable=bare-except
            LOGGER.debug("Get request: unknown exception occurred")
            return None

    async def _async_post_request(self, suffix:str, json_body:str={}) -> bool | None:
        """Generic POST method."""
        url = "http://" + self._host + str(suffix)

        try:
            async with self._session.post(
                url=url, json=json_body, allow_redirects=False, timeout=2
            ) as response:
                response_data = await response.text()
                LOGGER.debug(
                    "Host %s: HTTP %s Response data: %s",
                    self._host,
                    response.status,
                    response_data,
                )

            return True

        except aiohttp.ClientConnectorError as conn_err:
            LOGGER.debug("Host %s: Connection error %s", self._host, str(conn_err))
            return False
        except asyncio.TimeoutError:
            LOGGER.debug(
                "Devialet connection timeout exception, please check the connection"
            )
            return False
        except (TypeError, json.JSONDecodeError):
            LOGGER.debug("Post request: unknown response type")
            return False
        except Exception:  # pylint: disable=bare-except
            LOGGER.debug("Post request: unknown exception occurred")
            return False

    async def _async_on_search_response(self, data: CaseInsensitiveDict) -> None:
        """UPnP device detected."""
        location = data['location']
        location_regex = re.compile(f"(?<=Location:[ ])*http://{self._host}:(.*)/.*.xml", re.IGNORECASE)
        location_result = location_regex.search(location)
        if location_result:
            requester = AiohttpRequester()
            factory = UpnpFactory(requester)
            self._upnp_device = await factory.async_create_device(location)
            self._dmr_device = DmrDevice(self._upnp_device, None)

    async def async_search_allowed(self) -> bool:
        """Conditions to check if UPnP search is allowed."""
        if (
            self.is_available
            and not self.upnp_available
            and self.is_system_leader
            and ( not self._last_upnp_search
            or ( datetime.datetime.now() - self._last_upnp_search).total_seconds() >= UPNP_SEARCH_INTERVAL ) ):
            return True
        return False

    async def async_discover_upnp_device(self) -> None:
        """Discover the UPnP device."""
        self._last_upnp_search = datetime.datetime.now()

        await async_search(async_callback=self._async_on_search_response,
                           timeout=10,
                           search_target=MEDIA_RENDERER,
                           source=("0.0.0.0", 0))
        LOGGER.debug("Discovering UPnP device for %s", self._host)

    async def async_play_url_source(self, media_url: str, media_title: str, meta_data: Union[None, str, Mapping] = None):
        """Play media uri over UPnP."""
        if not self.upnp_available:
            LOGGER.error("No UPnP location discovered")
            return

        service = self._upnp_device.service(AV_TRANSPORT)
        set_uri = service.action("SetAVTransportURI")

        try:
            result = await set_uri.async_call(InstanceID=0, CurrentURI=media_url, CurrentURIMetaData=meta_data)
            LOGGER.debug("Action result: %s", str(result))
        except UpnpActionResponseError as a:
            LOGGER.error("Error playing %s: %s", media_title, a.error_desc)
            return
        except UpnpXmlParseError as x:
            LOGGER.error("Error playing %s %s", media_title, x.text)
            return

        await self.async_upnp_play()

    async def async_upnp_play(self) -> None:
        """Send the play command over UPnP."""
        if not self.upnp_available:
            LOGGER.error("No UPnP location discovered")
            return

        service = self._upnp_device.service(AV_TRANSPORT)
        set_uri = service.action("Play")

        try:
            await set_uri.async_call(InstanceID=0, Speed="1")
            return
        except UpnpActionResponseError:
            return
        except UpnpXmlParseError:
            return

    async def async_get_upnp_media_title(self, url: str) -> str | None:
        """Call the media URL with the HEAD method to get ICY metadata."""
        try:
            async with self._session.head(
                url=url, allow_redirects=False, timeout=2, headers={"Icy-MetaData": "1"}
            ) as response:
                LOGGER.debug(
                    "Host %s: HTTP Response data: %s",
                    self._host,
                    response.headers,
                )
            title:str = response.headers.get("icy-name")
            return title

        except aiohttp.ClientConnectorError:
            return
        except asyncio.TimeoutError:
            return
        except TypeError:
            return
        except Exception:  # pylint: disable=bare-except
            return
