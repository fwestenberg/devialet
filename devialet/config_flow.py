"""Support for Devialet Phantom speakers."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.const import CONF_IP_ADDRESS, CONF_SCAN_INTERVAL
from homeassistant.components import zeroconf

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL, LOGGER
from .devialet_api import DevialetApi


class DevialetFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for devialet."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize flow."""
        self._host: str = ""
        # self._mac: str | None = None
        self._name: str | None = None
        self._model: str | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by the user."""
        errors = {}

        if user_input is not None:
            session = async_get_clientsession(self.hass)
            api = DevialetApi(user_input[CONF_IP_ADDRESS], session)

            if not await api.async_update() or api.device_id is None:
                errors["base"] = "cannot_connect"
                LOGGER.error("Cannot connect")
            else:
                await self.async_set_unique_id(api.device_id)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=user_input[CONF_IP_ADDRESS], data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_IP_ADDRESS): str,
                    vol.Optional(
                        CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                    ): int,
                }
            ),
            errors=errors,
        )

    async def async_step_zeroconf(
        self, discovery_info: zeroconf.ZeroconfServiceInfo
    ) -> FlowResult:
        """Handle a flow initialized by zeroconf discovery."""
        LOGGER.info("Devialet device found via ZEROCONF: %s", discovery_info)

        errors = {}
        self._host = discovery_info.host
        self._name = discovery_info.name.split(".", 1)[0]
        self._model = discovery_info.properties["model"]

        session = async_get_clientsession(self.hass)
        api = DevialetApi(self._host, session)

        if not await api.async_update() or api.device_id is None:
            errors["base"] = "cannot_connect"
            LOGGER.error("Cannot connect")
        else:
            await self.async_set_unique_id(api.device_id)
            self._abort_if_unique_id_configured()

        self.context["title_placeholders"] = {"device": self._host}
        return await self.async_step_confirm()

    async def async_step_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle user-confirmation of discovered node."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=f"{self._name} ({self._model})",
                data={
                    CONF_IP_ADDRESS: self._host,
                },
            )

        return self.async_show_form(
            step_id="confirm",
            description_placeholders={"name": f"{self._name} ({self._model})"},
            errors=errors,
        )
