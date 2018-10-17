#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from toolkit import ADB
from toolkit import Fastboot

from os import system
import sys
from time import sleep


def logo():
    print("""


   _____                      _       ______ _           _               
  / ____|                    | |     |  ____| |         | |              
 | (___  _ __ ___   __ _ _ __| |_    | |__  | | __ _ ___| |__   ___ _ __ 
  \___ \| '_ ` _ \ / _` | '__| __|   |  __| | |/ _` / __| '_ \ / _ \ '__|
  ____) | | | | | | (_| | |  | |_    | |    | | (_| \__ \ | | |  __/ |   
 |_____/|_| |_| |_|\__,_|_|   \__|   |_|    |_|\__,_|___/_| |_|\___|_|   
                                                                       
                                                                    V0.1


author: pyshivam<pyshivam.py@gmail.com>

""")


def smart_help():
    print("""
Code :
     1) ADB Devices        : Get list of all the adb devices.
     2) Fastboot Devices   : Get list of all fastboot devices.
     00) Clear             : Clear the screen.
""")


def clear():
    system("clear")
    logo()


def start():
    while True:
        choice = input("SFlasher@pyshivam:~# ").lower()
        if choice == "1" or choice == "devices":
            print(adb.get_devices())
        elif choice == "2" or choice == "fastboot devices":
            print(fastboot.get_devices())
        elif choice == "00" or choice == "clear":
            clear()
        else:
            print("Command not found...")


if __name__ == '__main__':
    adb = ADB()
    fastboot = Fastboot()
    try:
        logo()
        start()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detect Exiting Tools . . .")
        sleep(2)
        sys.exit()
