"""Constants for the Devialet integration."""
import logging
from enum import Enum

LOGGER = logging.getLogger(__package__)

NORMAL_INPUTS = {
    "Airplay": "airplay2",
    "Bluetooth": "bluetooth",
    "Digital left": "digital_left", #Arch only
    "Digital right": "digital_right", #Arch only
    "Line": "line", #Arch only
    "UPnP": "upnp",
    "Optical": "optical", #Phantom I, Dialog (Mono)
    "Optical left": "optical_left", #Phantom I (Stereo)
    "Optical right": "optical_right", #Phantom I (Stereo)
    "Optical jack": "opticaljack", #Phantom II (Mono)
    "Optical jack left": "opticaljack_left", #Phantom II (Stereo)
    "Optical jack right": "opticaljack_right", #Phantom II (Stereo)
    "Phono": "phono", #Arch only
    "Raat": "raat",
    "Spotify Connect": "spotifyconnect",
}

SPEAKER_POSITIONS = {
    "FrontLeft": "left",
    "FrontRight": "right",
}

AV_TRANSPORT = "urn:schemas-upnp-org:service:AVTransport:2"
MEDIA_RENDERER = "urn:schemas-upnp-org:device:MediaRenderer:2"

class UrlSuffix(Enum):
    # Devices commands
    GET_GENERAL_INFO = "/ipcontrol/v1/devices/current"

    # Systems commands
    GET_VOLUME = "/ipcontrol/v1/systems/current/sources/current/soundControl/volume"
    GET_NIGHT_MODE = "/ipcontrol/v1/systems/current/settings/audio/nightMode"
    GET_EQUALIZER = "/ipcontrol/v1/systems/current/settings/audio/equalizer"
    TURN_OFF = "/ipcontrol/v1/systems/current/powerOff"
    VOLUME_UP = "/ipcontrol/v1/systems/current/sources/current/soundControl/volumeUp"
    VOLUME_DOWN = (
        "/ipcontrol/v1/systems/current/sources/current/soundControl/volumeDown"
    )
    VOLUME_SET = "/ipcontrol/v1/systems/current/sources/current/soundControl/volume"
    EQUALIZER = "/ipcontrol/v1/systems/current/settings/audio/equalizer"
    NIGHT_MODE = "/ipcontrol/v1/systems/current/settings/audio/nightMode"
    SELECT_SOURCE = "/ipcontrol/v1/groups/current/sources/%SOURCE_ID%/playback/play"

    # Groups commands
    GET_SOURCES = "/ipcontrol/v1/groups/current/sources"
    GET_CURRENT_SOURCE = "/ipcontrol/v1/groups/current/sources/current"
    GET_CURRENT_POSITION = (
        "/ipcontrol/v1/groups/current/sources/current/playback/position"
    )
    SEEK = "/ipcontrol/v1/groups/current/sources/current/playback/position"
    PLAY = "/ipcontrol/v1/groups/current/sources/current/playback/play"
    PAUSE = "/ipcontrol/v1/groups/current/sources/current/playback/pause"
    STOP = "/ipcontrol/v1/groups/current/sources/current/playback/pause"
    PREVIOUS_TRACK = "/ipcontrol/v1/groups/current/sources/current/playback/previous"
    NEXT_TRACK = "/ipcontrol/v1/groups/current/sources/current/playback/next"
    MUTE = "/ipcontrol/v1/groups/current/sources/current/playback/mute"
    UNMUTE = "/ipcontrol/v1/groups/current/sources/current/playback/unmute"

    def __str__(self):
        return str(self.value)
