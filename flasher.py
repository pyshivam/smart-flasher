#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from toolkit import ADB
from toolkit import Fastboot

from os import system
import sys
from time import sleep
import json


def logo():
    clear()
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
     99) Exit              : Exit from tool. 
""")


def clear():
    system("clear")


def start():
    while True:
        choice = input("SFlasher@pyshivam:~# ").lower()
        if choice == "1" or choice == "devices":
            adb_operations()
        elif choice == "2" or choice == "fastboot devices":
            fastboot_operations()
        elif choice == "00" or choice == "clear":
            clear()
        elif choice == "99" or choice == "exit":
            print("Exiting tool.. \nThanks for using smart flasher.")
            sys.exit(0)
        else:
            print("Command not found...")


def adb_operations(mode=1):
    # print(adb.get_devices())
    pass


def fastboot_operations(mode=1):
    # print(fastboot.get_devices())
    pass


def config_loader(device):
    pass


if __name__ == '__main__':
    adb = ADB()
    fastboot = Fastboot()
    try:
        logo()
        start()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected Exiting Tools . . .")
        sleep(1)
        sys.exit()
    except EOFError:
        print("\n[!] CTRL+Z Detected Exiting Tools . . .")
        sleep(1)
        sys.exit()
