#! /usr/bin/bash
. ~/RPi0-vehicle/venv/bin/activate
echo "Starting pigpio daemon"
sudo pigpiod
echo "Starting camera stream server"
raspivid -ISO 0 -t 0 -n -o - -w 640 -h 480 -fps 10 -b 25000000 -cd MJPEG | raspivid_mjpeg_server &
cd ~/RPi0-vehicle/RPi0-vehicle-dev
python stream_server.py &
python vehicle_ws_server.py &
python -m http.server --directory ./www &

