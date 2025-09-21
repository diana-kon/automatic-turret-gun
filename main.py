#!/usr/bin/env python

import math
import time
from blinker import BLACK, RED, GREEN, PURPLE, slide, scroll, Color
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
    for i in range(8):
        blinkt.clear()
        blinkt.set_pixel(i, 255, 0, 0, 0.2)
        blinkt.show()


def change_lights(lights: list[Color]):
    for i, light in enumerate(lights):
        blinkt.set_pixel(i, light.r, light.g, light.b, 0.1)
    blinkt.show()


def main():
    log = logger.create_logger(logger.DataDogHandler())
    log.info("it started successfully, changed")
    a = 0
    step = 0.25
    n = 0
    pantilthat.pan(a)
    pantilthat.tilt(-20)
    cycle = 0
    lights = [PURPLE, GREEN, PURPLE, PURPLE, PURPLE, PURPLE, PURPLE, PURPLE]
    while True:
        # blink()
        change_lights(lights)
        lights = scroll(lights)
        time.sleep(0.5)
        #(a, step, n) = move(a, step, n)
        #if (a == 0 and step < 0):
        cycle = cycle + 1
        if cycle > 32:
            log.info("it shut down gracefully")
            break

main()
