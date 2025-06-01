#!/usr/bin/env python

import math
import time

import pantilthat

def angle(current, step):
    if (current >= 60 or current <= -60):
        step = 0 - step
    return (current + step, step)

def move(a, step, n):
    (a, step) = angle(a, step)
    pantilthat.pan(a)
    pantilthat.tilt(-20)
    if (a % 30 == 0):
        time.sleep(2)
    else:
        time.sleep(0.003)
    return (a, step, n + 1)

def main():
    a = 0
    step = 0.25
    n = 0
    cycle = 0
    while True:
        (a, step, n) = move(a, step, n)
        if (a == 0 and step < 0):
            cycle = cycle + 1
        if (cycle > 2):
            break

main()
