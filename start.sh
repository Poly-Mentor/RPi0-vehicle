#! /usr/bin/bash
#https://github.com/kig/raspivid_mjpeg_server
sudo pigpiod
cd /home/fs/raspivid_mjpeg_server
raspivid -ISO 0 -t 0 -n -o - -w 640 -h 480 -fps 10 -b 25000000 -cd MJPEG | cargo run --release &
cd /home/fs/vehicle
python3 vehicle_ws_server.py &
python3 -m http.server --directory /home/fs/vehicle/www &

