#!/bin/bash
echo "Starting installation"
cd ~
cd "Installing camera apps"
sudo apt install libcamera-apps -y
# echo "Installing ffmpeg"
# sudo apt-get install ffmpeg -y
# echo "Installing pigpio"
# sudo apt install pigpio -y
# echo "Installing VLC"
# sudo apt install vlc -y
echo "Installing python3-picamera2"
sudo apt install -y python3-picamera2 --no-install-recommends
echo "Installing OpenCV"
sudo apt install python3-opencv -y
echo "Installing Flask"
sudo apt install python3-flask -y
echo "Downloading sources"
curl -L -o repo.zip "https://github.com/Poly-Mentor/RPi0-vehicle/archive/refs/heads/dev.zip"
echo "Unzipping sources"
unzip repo.zip -d RPi0-vehicle
echo "Removing archive"
rm repo.zip
# echo "Installing PIP (Python package manager)"
# sudo apt-get install python3-pip -y
# echo "Creating Python virtual environment"
cd ~/RPi0-vehicle
# python -m venv --system-site-packages venv
# echo "Activating virtual environment and installing Python dependencies"
# . venv/bin/activate && pip install -r requirements.txt