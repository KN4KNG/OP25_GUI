#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  OP25_GUI.py
#  
#  Copyright 2019  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import tkinter as tk
import subprocess
import os
import threading

#Commands

def stopall():
    os.system("pkill -f ./rx.py")
def CMD_OP25_01():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.75e6 -o 25000 -q 1 -T Berea.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_02():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.6125e6 -o 25000 -q 1 -T Butner.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_03():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.975e6 -o 25000 -q 1 -T Bullock_WICE_FM.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_04():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.6375e6 -o 25000 -q 1 -T Oak_Hill.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_05():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 852.975e6 -o 25000 -q 1 -T Oxford_Water_Tower.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_06():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.8875e6 -o 25000 -q 1 -T Oxford_Bi-Com.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_07():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 773.53125e6 -o 25000 -q 1 -T Manson.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_08():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 853.675e6 -o 25000 -q 1 -T Roxboro_1.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_09():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 774.63125e6 -o 25000 -q 1 -T Roxboro_2.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_10():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 769.26875e6 -o 25000 -q 1 -T Mt_Tirzah.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_11():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 852.1375e6 -o 25000 -q 1 -T Louisburg.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_12():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 774.83125e6 -o 25000 -q 1 -T Youngsville.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_13():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 858.8375e6 -o 25000 -q 1 -T Duke_University.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_14():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 858.8125e6 -o 25000 -q 1 -T Camden_Ave.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_15():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 859.5125e6 -o 25000 -q 1 -T Cole_Mill_Rd.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_16():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 774.2875e6 -o 25000 -q 1 -T Brian_Center.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_17():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 859.2625e6 -o 25000 -q 1 -T Eno_Mtn.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_18():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 859.7625e6 -o 25000 -q 1 -T Laws.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_19():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 774.39375e6 -o 25000 -q 1 -T Mebane.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")
def CMD_OP25_20():
    os.system("pkill -f ./rx.py") 
    os.system("cd ~/op25/op25/gr-op25_repeater/apps; ./rx.py --args 'rtl' -N 'LNA:47' -S 2400000 -f 860.4625e6 -o 25000 -q 1 -T Wake_North_Durant.tsv -V -2 -U 2> stderr.2 -l 'http:0.0.0.0:8080'&")

def main():
    mw = tk.Tk()

    #Specify the attributes for all widgets simply like this.
    mw.option_add("*Button.Background", "Teal")
    mw.option_add("*Button.Foreground", "White")

    mw.title('OP25 Repeater Selector GUI')
    #You can set the geometry attribute to change the root windows size
    mw.geometry("750x580") #You want the size of the app to be 750 X 562.5 Pixels (Slightky Smaller than the RPI 7" Touch Screens)
    mw.resizable(0, 0) #Don't allow resizing in the x or y direction

    back = tk.Frame(master=mw,bg='Grey')
    back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
    back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window


    #Buttons

    Stop_OP25 = tk.Button(master=back, text='Stop OP25 Instances', command=stopall, width=14, height=5)
    Stop_OP25.grid(row=0, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_01 = tk.Button(master=back, text='Berea', command=CMD_OP25_01, width=14, height=5)
    OP25_01.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_02 = tk.Button(master=back, text='Butner', command=CMD_OP25_02, width=14, height=5)
    OP25_02.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_03 = tk.Button(master=back, text='Bullock WICE FM', command=CMD_OP25_03, width=14, height=5)
    OP25_03.grid(row=1, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_04 = tk.Button(master=back, text='Oak Hill', command=CMD_OP25_04, width=14, height=5)
    OP25_04.grid(row=1, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_05 = tk.Button(master=back, text='Oxford Water Tower', command=CMD_OP25_05, width=14, height=5)
    OP25_05.grid(row=1, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_06 = tk.Button(master=back, text='Oxford Bi-Com', command=CMD_OP25_06, width=14, height=5)
    OP25_06.grid(row=2, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_07 = tk.Button(master=back, text='Manson', command=CMD_OP25_07, width=14, height=5)
    OP25_07.grid(row=2, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_08 = tk.Button(master=back, text='Roxboro 1', command=CMD_OP25_08, width=14, height=5)
    OP25_08.grid(row=2, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_09 = tk.Button(master=back, text='Roxboro 2', command=CMD_OP25_09, width=14, height=5)
    OP25_09.grid(row=2, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_10 = tk.Button(master=back, text='Mt.Tirzah', command=CMD_OP25_10, width=14, height=5)
    OP25_10.grid(row=2, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_11 = tk.Button(master=back, text='Louisburg', command=CMD_OP25_11, width=14, height=5)
    OP25_11.grid(row=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_12 = tk.Button(master=back, text='Youngsville', command=CMD_OP25_12, width=14, height=5)
    OP25_12.grid(row=3, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_13 = tk.Button(master=back, text='Duke University', command=CMD_OP25_13, width=14, height=5)
    OP25_13.grid(row=3, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_14 = tk.Button(master=back, text='Camden Ave.', command=CMD_OP25_14, width=14, height=5)
    OP25_14.grid(row=3, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_15 = tk.Button(master=back, text='Cole Mill Rd.', command=CMD_OP25_15, width=14, height=5)
    OP25_15.grid(row=3, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_16 = tk.Button(master=back, text='Brian Center', command=CMD_OP25_16, width=14, height=5)
    OP25_16.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_17 = tk.Button(master=back, text='Eno Mtn.', command=CMD_OP25_17, width=14, height=5)
    OP25_17.grid(row=4, column=2, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_18 = tk.Button(master=back, text='Laws', command=CMD_OP25_18, width=14, height=5)
    OP25_18.grid(row=4, column=3, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_19 = tk.Button(master=back, text='Mebane', command=CMD_OP25_19, width=14, height=5)
    OP25_19.grid(row=4, column=4, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    OP25_20 = tk.Button(master=back, text='Wake North Durant', command=CMD_OP25_20, width=14, height=5)
    OP25_20.grid(row=4, column=5, sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)
    close = tk.Button(master=back, text='Quit', command=mw.destroy)
    close.pack(side='bottom')
    info = tk.Label(master=back, text='Created By:', bg='Teal', fg='black')
    info1 = tk.Label(master=back, text='Alex Bowman - KN4KNG', bg='Teal', fg='black')
    info2 = tk.Label(master=back, text='KN4KNG@Outlook.com', bg='Teal', fg='black')
    info2.pack(side='bottom')
    info1.pack(side='bottom')
    info.pack(side='bottom')

    mw.mainloop()

if __name__ == '__main__':
    main()

