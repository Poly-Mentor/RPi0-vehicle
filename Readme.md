# Raspberry Pi controlled vehicle

## Features
- Open source
- 3D printed construction
- 4 geared DC motors
- TPU printed one-part "tracks" 
- powered by 6V sealed acid battery
- [ORP](https://openroboticplatform.com/) compatible mounting points (easy to expand)
- Raspberry Pi Zero W
- custom robot controller HAT
- camera
- LED lights
- web interface

## Features to be added
- power management (battery voltage monitoring, automatic shutdown, current draw monitoring)
- rotable camera mount
- LIDAR [D200 WaveShare](https://www.waveshare.com/wiki/D200_LiDAR_Kit)
- advanced indoor positioning system

## Software installation

1. Use Raspberry Pi Imager to install Raspberry Pi OS on microSD card. Choose Lite version of system (bookworm) and pre-configure it for headless operation (WiFi credentials, username, password, enable SSH).
2. Plug in microSD card into Raspberry Pi, wait for it to boot.
3. Find an IP address of your RPi and connect to it via SSH.
4. Update system:

    ```
    sudo apt-get update && sudo apt-get upgrade
    ```

5. Download and run installation script:

    ⚠️ it may take long time to complete, so be patient

    ```
    wget https://raw.githubusercontent.com/Poly-Mentor/RPi0-vehicle/main/install.sh && chmod +x install.sh && bash install.sh
    ```