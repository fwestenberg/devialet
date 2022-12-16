# Devialet
Devialet API Python implementation

This is the first working version, a lot of things still need to be improved. Please be patient.

# Installation instructions
- Add the `devialet` folder to your `config/custom_components/` folder
- Restart HA
- The Devialet device(s) will automatically be discovered

If discovery did not complete within 1-2 minutes:
- Add the device using the config flow

# Known issues:
- When using Airplay, no media art is available (due to the API)
- Select source not working (due to the API)
