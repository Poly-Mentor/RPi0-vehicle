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

## Future plans
- power management (battery voltage monitoring, automatic shutdown, current draw monitoring)
- rotable camera mount
- LIDAR [D200 WaveShare](https://www.waveshare.com/wiki/D200_LiDAR_Kit)
- advanced indoor positioning system

## Software installation

1. Use Raspberry Pi Imager to install Raspberry Pi OS Lite Legacy (**Bullseye**, it won't work on Bookworm and later!) on microSD card. Pre-configure it for headless operation (WiFi credentials, username, password, enable SSH).
2. Plug in microSD card into Raspberry Pi, wait for it to boot.
3. Find an IP address of your RPi and connect to it via SSH.
4. Update system:

    ```
    sudo apt-get update && sudo apt-get upgrade -y
    ```

<!-- 5. Enable legacy camera stack

    ```
    sudo raspi-config
    ```

    select `Interface options -> Legacy camera support` and enable it
    go back to main menu, finish and reboot -->

5. Download and run installation script:

    ⚠️ it may take long time to complete, so be patient

    ```
    wget https://raw.githubusercontent.com/Poly-Mentor/RPi0-vehicle/dev/install.sh && chmod +x install.sh && bash install.sh
    ```

6. (optional) Save compiled binary

    If you want to avoid long re-building raspivid_mjpeg_server after OS reinstallation, you can zip it:

    ```
    zip -r ~/raspivid_mjpeg_server_bin.zip ~/raspivid_mjpeg_server/raspivid_mjpeg_server-master/target/release/raspivid_mjpeg_server 
    ```
    then copy it to your PC or pendrive.
    
    After system reinstallation, just copy it to your home directory. `install.sh` script will recognize it, unzip, and install this version without downloading Rust and compiling.


## Credits

- [Pithikos](https://github.com/Pithikos) for his [Python Websocket Server](https://github.com/Pithikos/python-websocket-server)
- [kig](https://github.com/kig) for [Raspivid MJPEG Server](https://github.com/kig/raspivid_mjpeg_server)