# OP25_GUI
Graphical User Interface for OP25

This is a personal project that I have made with tkinter to allow for a raspbery pi w/ 7" touchscreen to interface with OP25 in a mobile/portable envirroment. There are two versions that I've made two types. The first type that I made only suppoerts twenty favorites, you will need to edit the file to meet you needs. You'll need to alter the offset to meet your device, frequency, audio output, button names ect. If you are in the state of North Carolina, you will benefit from my second project, The cseond has two python files, one for USB audio output and the other default analog/HDMI output, whichever is set to default on your Raspberry Pi. 

This Project will only work if you install the op25 as per the developer. The working directory of the OP25 rx.py is: /home/pi/op25/op25/gr-op25_repeater/apps. If you have any deviation please update the OP25_GUI.py to meet your requirements.

To set up for the North Carolina counties file:

Boot your pi, open a terminal and type the following commands.

*sudo apt update*
*sudo apt install gnuradio libvolk1-bin libusb-1.0-0 gr-iqbal*
*sudo apt install qt5-default libqt5svg5 libportaudio2*
*sudo cp udev/*.rules /etc/udev/rules.d/*

Now make a directory and download gqrx

*cd*
*mkdir gqrx*
*cd gqrx*
*wget https://github.com/csete/gqrx/releases/download/v2.11.5/gqrx-sdr-2.11.5-linux-rpi3.tar.xz*

Download OP25 from the repository using this command. Make sure you change directories out of gqrx.

*cd*
*git clone https://github.com/boatbod/op25.git*

It will make a folder called op25

*cd op25*

*./install.sh*

It will instruct you to install GNUPLOT following the build and install process

*sudo apt-get install gnuplot-x11*

Wait a bit for it to install.  It should take care of everything.

Once you have OP25 installed, Download the files contained in this github. Copy the NC_Viper folder to:

*/home/pi/op25/op25/gr-op25_repeater/apps*

Then Copy North_Carolina_Viper_GUI_Non_USB_Speaker_Default_Audio.py or North_Carolina_Viper_GUI.py to you desktop.

Next you will need to make these python files executabble. Open a terminal and do the following.

*cd Desktop*

*chmod +x *.py*

(This will make all of your python files on your desktop executable)
If you have other python files you do not want to make executables do the following.

*cd Desktop*

*chmod +x North_Carolina_Viper_GUI_Non_USB_Speaker_Default_Audio.py*
*chmod +x North_Carolina_Viper_GUI.py*

You should now be complete. Click on the appropiate .py to start. Once OP25 is started by clicking a button yo may open your broweser and navigate to 127.0.0.1:8080 to go to the http dashboard created by BoatBod/Osmocom depending on the version you are using. 

If you are using a touchscreen that is HDMI or if you need to enable the aux port as the default enter the following command:

*sudo amixer cset numid=3 <output>*

*0=auto*
*1=aux*
*2=hdmi*

I am not conitnuing development on this project at the moment. Please make this project your own and redistribute it. There is just too much going on in my life to keep up with this development. 

73's and happy scanning. 

<img src="https://i.creativecommons.org/p/mark/1.0/88x31.png" alt="PDM">

<img src="https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-9/67118050_10156090905340810_8713265728955875328_o.jpg?_nc_cat=104&_nc_oc=AQnpYVZO9JFaPjmzhS6ZpHLRRUtiYPIJjDIOkBlOPDpr-U3xDqSG7Uay4_YOBmXu4uY&_nc_ht=scontent-iad3-1.xx&oh=fdc3c6aee924623481888930fd5d5706&oe=5DAE294C">
