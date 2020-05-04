#!/bin/bash

cd /home/pi
sudo cp /home/pi/OP25_GUI/tgid.tsv /home/pi/op25/op25/gr-op25_repeater/apps/
sudo cp -r /home/pi/OP25_GUI/NC_Counties_GUI/NC_Viper/ /home/pi/op25/op25/gr-op25_repeater/apps/
sudo cp /home/pi/OP25_GUI/NC_Counties_GUI/*.py /home/pi/Desktop/
sudo chmod 777 /home/pi/Desktop/North_Carolina_Viper_GUI_Non_USB_Speaker_Default_Audio.py
sudo chmod 777 /home/pi/Desktop/North_Carolina_Viper_GUI.py
