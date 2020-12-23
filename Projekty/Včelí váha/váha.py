#!/usr/bin/python3 -u
from Bluetooth_třída import BluetoothComm
from time import sleep
import subprocess

with BluetoothComm() as comm:
    while True:
        # comm.send_comm("ahoj jak terminal jede?\n")
        comm.send_comm("mehehe")
        read = comm.read_comm()
        print(f"Input: {read}")
        if read == b"turn off\r\n":
            subprocess.run(["poweroff"])
            break
        elif read == b'q\r\n':
            print("program ukončen")
            break
        sleep(.1)
