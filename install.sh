#!/bin/bash
echo "Starting installation"
cd ~
echo "Installing pigpio"
sudo apt install pigpio -y
echo "Downloading sources"
curl -L -o repo.zip "https://github.com/Poly-Mentor/RPi0-vehicle/archive/refs/heads/main.zip"
echo "Unzipping sources"
unzip repo.zip -d RPi0-vehicle
echo "Removing archive"
rm repo.zip

# if raspivid_mjpeg_server_bin.zip exists, unzip it
if [ -f "raspivid_mjpeg_server_bin.zip" ]; then
    unzip raspivid_mjpeg_server_bin.zip -d raspivid_mjpeg_server
    cd raspivid_mjpeg_server
    sudo cp raspivid_mjpeg_server/raspivid_mjpeg_server /usr/local/bin
# else download sources and compile it
else
    curl -L -o repo2.zip "https://github.com/kig/raspivid_mjpeg_server/archive/refs/heads/master.zip"
    echo "Unzipping sources"
    unzip repo2.zip -d raspivid_mjpeg_server
    echo "Removing archive"
    rm repo2.zip
    echo "Installing Rust"
    curl https://sh.rustup.rs -sSf | sh
    . ~/.cargo/env
    echo "Building camera server"
    cd ~/raspivid_mjpeg_server/raspivid_mjpeg_server-master
    cargo build --release
    echo "Installing camera server"
    sudo cp target/release/raspivid_mjpeg_server /usr/local/bin
fi

echo "Installing Python dependencies: PIP and venv"
sudo apt-get install python3-pip python3-venv -y
echo "Creating Python virtual environment"
cd ~/RPi0-vehicle
python -m venv --system-site-packages venv
echo "Activating virtual environment and installing Python dependencies"
. venv/bin/activate && pip install -r RPi0-vehicle-main/requirements.txt