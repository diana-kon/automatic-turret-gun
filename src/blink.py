#!/usr/bin/env python

import time
from multiprocessing import Process

import blinkt

def blink(on = True):
    color = 55
    if (not on):
        color = 0
    blinkt.set_pixel(0, color, 0, 0, 0.1)
    blinkt.show()
    time.sleep(1)
    return not on

def main():
    on = True
    while True:
        on = blink(on)

main()
