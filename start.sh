#! /usr/bin/bash
sudo pigpiod
#rpicam-vid --nopreview -t 0 --width 1296 --height 972 --framerate 10 --inline --listen -o tcp://0.0.0.0:5555
raspilive 
cd ~/RPi0-vehicle
python stream_server.py &
# python vehicle_ws_server.py &
# python -m http.server --directory /home/fs/vehicle/www &

