"""Support for Devialet Phantom speakers."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult
from homeassistant.const import CONF_IP_ADDRESS, CONF_SCAN_INTERVAL

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL


class DevialetFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for devialet."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by the user."""
        if user_input is not None:
            await self.async_set_unique_id("fnjwek347892347")
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
        )
