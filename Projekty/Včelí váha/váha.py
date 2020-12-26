#!/usr/bin/python3 -u
from Bluetooth_třída import BluetoothComm
from time import sleep
import subprocess
from gpiozero import PWMLED
from typing import List, Union


def bytes_find(inp: bytes, find: Union[bytes, List[bytes]]) -> float:
    for i in find:
        index = inp.find(i)
        if index != -1:
            break
    # noinspection PyUnboundLocalVariable
    return float(inp[index:])


led = PWMLED(4)
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
        elif b'led' in read:
            if b'on' in read:
                led.on()
            elif b'toggle' in read:
                led.toggle()
            elif b'off' in read:
                led.off()
            elif b'value' in read:
                led.value = bytes_find(read, [b'.', b'1', b'0'])

        sleep(.1)
