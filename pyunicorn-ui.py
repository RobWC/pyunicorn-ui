#!/usr/bin/env python

import unicornhat
import time
import random

class UnicornHatManager:
    def __init__(self, brightness):
        unicornhat.brightness(brightness)
    def set_rotation(self,rotation):
        unicornhat.rotation(rotation)
    def set_pixel(self, x,y,r,b,g):
        unicornhat.set_pixel(x,y,r,b,g)
        unicornhat.show()

um = UnicornHatManager(0.1)
um.set_rotation(0)

heart = [[0, 1, 1, 0, 0, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0]]

def random_color():
    return random.randrange(0,255)

def random_pattern():
    for x in range(0,8):
        for y in range (0,8):
            r = random_color()
            g = random_color()
            b = random_color()
            um.set_pixel(x,y,r,g,b)


def draw_heart():
    for x in range(0,8):
     for y in range(0,8):
         if heart[x][y]:
             if x == 0:
                 r, g, b = 255, 0, 0
             elif  x == 1:
                 r, g, b = 240, 128,0
             elif  x == 2:
                 r, g, b = 255, 255, 0
             elif  x == 3:
                 r, g, b = 0, 255, 0
             elif  x == 4:
                 r, g, b = 0, 0, 255
             elif  x == 5:
                 r, g, b = 127, 0, 255
             elif  x == 6:
                 r, g, b = 255, 0, 255
             elif  x == 7:
                 r, g, b = 255, 0, 127
             um.set_pixel(x,y,r,g,b)

while True:
    random_pattern()
    time.sleep(1)

#draw_heart()
#time.sleep(0.1)
#unicornhat.clear()

'''
while True:
    um.set_rotation(90)
    draw_heart()
    time.sleep(0.1)
    unicornhat.clear()
    um.set_rotation(180)
    draw_heart()
    time.sleep(0.1)
    unicornhat.clear()
    um.set_rotation(270)
    draw_heart()
    time.sleep(0.1)
    unicornhat.clear()
    um.set_rotation(0)
    draw_heart()
    time.sleep(0.1)
    unicornhat.clear()
'''
