# OP25_GUI
Graphical User Interface for OP25

This is a personal project that I have made with tkinter to allow for a raspbery pi w/ 7" touchscreen to interface with OP25 in a mobile/portable envirroment. 

This Project will only work if you install the op25 as per the developer. The working directory of the OP25 rx.py is: /home/pi/op25/op25/gr-op25_repeater/apps. If you have any deviation please update the OP25_GUI.py.

Currently there is support for 20 sites. 

You will need to create a separate .tsv file and name the in the manner which you will use in the commands. The .tsv files I am using are uploaded and will work for you if you are in the Wake, Granvile, Durham or Orange COunties of North Craolina, USA. The .py GUI file can be saved any where. The .tsv files will need to be saved in the /home/pi/op25/op25/gr-op25_repeater/apps/ direcotry.

Once that is completed, rename the button labels and update the commands with the desired site .tsv. Also, update any arguments in the command ie; SDR type, hardware output for audio (I'm using hw=1,0 for usb speakers ATM), etc.

I am currently looking into creating a set up file to allow for ease of creation of your own GUI without having to alter any code. I will work on this as time allows. 

If you have any interest in assisting with this project, please feel free to reach out to me.

73's and happy scanning. 

<img src="https://i.creativecommons.org/p/mark/1.0/88x31.png" alt="PDM">

<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fphoto.php%3Ffbid%3D10155983450435810%26set%3Da.10150237747365810%26type%3D3&width=500" width="500" height="676" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media"></iframe>
