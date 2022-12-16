# Devialet
Devialet API Python implementation

This is the first working version, a lot of things still need to be improved. 
Also make sure your Devialet firmware version >= 2.16.1. Otherwise expect functions not to work.

# Installation instructions
- Add the `devialet` folder to your `config/custom_components/` folder
- Restart HA
- The Devialet device(s) will automatically be discovered
- If discovery did not complete within 1-2 minutes, add the device using the config flow
- For a stereo setup, only one of the speakers need to be configured

# Known issues:
- When using Airplay, no media art is available
- Select source not working


# Screenshots:

## Discovery

<img width="297" alt="image" src="https://user-images.githubusercontent.com/47930023/208066307-24cc39eb-6f21-47a5-9674-5e3f0996e4b0.png">

<img width="418" alt="image" src="https://user-images.githubusercontent.com/47930023/208066552-fcd21bf9-a8ad-400a-8a60-04250e6c296e.png">


## Manual configuration

<img width="405" alt="image" src="https://user-images.githubusercontent.com/47930023/208067522-3b416cda-a4aa-4d8a-b3a5-fea23b0a81d9.png">


## Device overview

<img width="825" alt="image" src="https://user-images.githubusercontent.com/47930023/208066755-b5c072bd-1a27-4947-be64-90d6a4e87c7d.png">

<img width="563" alt="image" src="https://user-images.githubusercontent.com/47930023/208066926-ee08cb60-29f1-4b33-950f-edc6ab5366c9.png">

<img width="488" alt="image" src="https://user-images.githubusercontent.com/47930023/208067167-a7ea516b-38f5-4cc8-84a0-6dffc8ed0639.png">
