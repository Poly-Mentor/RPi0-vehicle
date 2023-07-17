#! /usr/bin/bash
#https://github.com/kig/raspivid_mjpeg_server
raspivid -ISO 0 -t 0 -n -o - -w 640 -h 480 -fps 10 -b 25000000 -cd MJPEG | raspivid_mjpeg_server

