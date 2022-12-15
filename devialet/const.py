"""Constants for the Devialet integration."""
import logging
from typing import Final

import datetime

DOMAIN: Final = "devialet"
DEFAULT_NAME: Final = "Devialet"
DEFAULT_SCAN_INTERVAL = 5
MANUFACTURER: Final = "Devialet"
LOGGER = logging.getLogger(__package__)

# UPNP_ST = "urn:schemas-upnp-org:device:MediaRenderer:2"
# DISCOVERY_INTERVAL = datetime.timedelta(seconds=60)

NORMAL_INPUTS = {
    "Airplay": "airplay2",
    "Bluetooth": "bluetooth",
    "Digital left": "digital_left",
    "Digital right": "digital_right",
    "Line": "line",
    "Online": "upnp",
    "Optical": "optical",
    "Optical left": "optical_left",
    "Optical right": "optical_right",
    "Optical jack": "opticaljack",
    "Phono": "phono",
    "Raat": "raat",
    "Spotify Connect": "spotifyconnect",
}

SOUND_MODES = {
    "Custom": "custom",
    "Flat": "flat",
    "Night mode": "night mode",
    "Voice": "voice",
}

SPEAKER_POSITIONS = {
    "FrontLeft": "left",
    "FrontRight": "right",
}
