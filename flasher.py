#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from toolkit import ADB
from toolkit import Fastboot

from os import system
import sys
from sys import platform as _platform
from time import sleep
import json


class Terminal:
    def __init__(self):
        if _platform == "linux" or _platform == "linux2":
            # linux
            self.cmd_clear = "clear"
        elif _platform == "darwin":
            # MAC OS X
            self.cmd_clear = "clear"
        elif _platform == "win32":
            # Windows
            self.cmd_clear = "cls"
        elif _platform == "win64":
            # Windows 64-bit
            self.cmd_clear = "cls"

    def clear(self):
        system(self.cmd_clear)


def logo():
    terminal.clear()
    print("""


   _____                      _       ______ _           _
  / ____|                    | |     |  ____| |         | |
 | (___  _ __ ___   __ _ _ __| |_    | |__  | | __ _ ___| |__   ___ _ __
  \___ \| '_ ` _ \ / _` | '__| __|   |  __| | |/ _` / __| '_ \ / _ \ '__|
  ____) | | | | | | (_| | |  | |_    | |    | | (_| \__ \ | | |  __/ |
 |_____/|_| |_| |_|\__,_|_|   \__|   |_|    |_|\__,_|___/_| |_|\___|_|

                                                                    V0.1


Author: Shivam Gupta (pyshivam)
Email: pyshivam.py@gmail.com
Github: https://www.github.com/pyshivam/
""")


def smart_help():
    logo()
    print("""
Code :
     1) ADB Devices        : Get list of all the adb devices.
     2) Fastboot Devices   : Get list of all fastboot devices.
     00) Clear             : Clear the screen.
     99) Exit              : Exit from tool.
""")


def start():
    while True:
        choice = input("SFlasher@pyshivam:~# ").lower()
        if choice == "1" or choice == "adb devices":
            adb_operations()
        elif choice == "2" or choice == "fastboot devices":
            fastboot_operations()
        elif choice == "3" or choice == "help":
            smart_help()
        elif choice == "00" or choice == "clear":
            terminal.clear()
        elif choice == "99" or choice == "exit":
            print("Exiting tool.. \nThanks for using smart flasher.")
            sys.exit(0)
        else:
            print("Command not found...")


def adb_operations(mode=1):
    devices = adb.get_devices_with_model()
    if devices is None:
        print("No device Found..")
    else:
        print(devices)
        for index, device in devices.items():
            print("%s\t%s" % (index, device))
    pass


def fastboot_operations(mode=1):
    # print(fastboot.get_devices())
    pass


def config_loader(device):
    pass


if __name__ == '__main__':
    terminal = Terminal()
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
