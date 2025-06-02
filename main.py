#!/usr/bin/env python

import math
import time

import logger

import pantilthat
import blinkt

def angle(current, step):
    if (current >= 90 or current <= -90):
        step = 0 - step
    return (current + step, step)

#def move(a, step, n):
#    (a, step) = angle(a, step)
    # do not control the pan-tilt for now
    # pantilthat.pan(a)
    # pantilthat.tilt(-20)
    #if (a % 45 == 0 or a == 0):
    #    blinkt.set_pixel(0, 156, 2, 163, 0.2)
    #    blinkt.show()
    #    time.sleep(2)
    #    blinkt.set_pixel(1, 0, 0, 0)
    #    blinkt.show()
    #else:
    #    time.sleep(0.003)
    #return (a, step, n + 1)



def blink():
    blinks = 0
    while True:
        for i in range(8):
            blinkt.clear()
            blinkt.set_pixel(i, 255, 0, 0, 0.2)
            blinks += 1
            blinkt.show()
            time.sleep(0.05)
        if blinks > 20:
            break
            #blinkt.show()





#def blink(timestamp):
#    if (timestamp % 2 == 0):
#        blinkt.set_pixel(1, 199, 38, 3, 0.1)
#    else:
#        blinkt.set_pixel(0, 0, 0, 0)
#    blinkt.show()

#Log_S

def main():
    log = logger.create_logger(logger.DataDogHandler())
    log.info("it started successfully, changed")
    a = 0
    step = 0.25
    n = 0
    cycle = 0
    while True:
        blink()
        #(a, step, n) = move(a, step, n)
        #if (a == 0 and step < 0):
        cycle = cycle + 1
        if cycle > 10:
            log.info("it shut down gracefully")
            break

main()
