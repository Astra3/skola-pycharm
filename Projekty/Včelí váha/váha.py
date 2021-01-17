#!/usr/bin/python3 -u
import logging
import subprocess
import sys
from time import sleep
from typing import List, Union

from Bluetooth_třída import BluetoothComm
from Měření import Vaha


def bytes_find(inp: bytes, find: Union[bytes, List[bytes]]) -> float:
    for i in find:
        index = inp.find(i)
        if index != -1:
            break
    # noinspection PyUnboundLocalVariable
    return float(inp[index:])


root = logging.getLogger()
root.setLevel(logging.DEBUG)

# Zajistí aby výstup logu šel do stdout a ne do stderr
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

with BluetoothComm() as comm, Vaha() as vaha:
    while True:
        comm.send(f"{vaha.read}\n")
        read = comm.read
        if b'raw' in read:
            comm.send(f"raw hodnota: {vaha.raw}")
        elif b'power off' in read or b'vypnout' in read:
            subprocess.run(["poweroff"])
        elif b'kalibrace' in read:
            comm.send(f"Kalibrační faktor: {vaha.calibration}")
        elif b"init read" in read:
            comm.send(f"Init reading: {vaha.init_reading}")
        elif b'q' in read:
            break
        sleep(.2)
