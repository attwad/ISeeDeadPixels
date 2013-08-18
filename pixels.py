#!/usr/bin/env python

"""Simple program that let you test if you have dead pixels on your screen.

Run this script and press any key to cycle through RGB-white-black colors full
screen, press ESCAPE to quit.
"""

import itertools

import pygame
from pygame import time
from pygame import display
from pygame import event
from pygame import locals


_Colors = [
    locals.Color(255, 0, 0),
    locals.Color(0, 255, 0),
    locals.Color(0, 0, 255),
    locals.Color(255, 255, 255),
    locals.Color(0, 0, 0)]


if __name__ == "__main__":
    pygame.init()
    clock = time.Clock()
    screen = display.set_mode(display.list_modes()[0], locals.FULLSCREEN)
    counter = itertools.count()
    color_index = 0
    color = _Colors[color_index]
    running = True
    while running:
      clock.tick(30)
      for evt in event.get():
        if evt.type == locals.QUIT:
          running = False
        elif evt.type == locals.KEYDOWN:
          if evt.key == locals.K_ESCAPE:
            running = False
          else:
            color_index += 1
            color = _Colors[color_index % len(_Colors)]
      screen.fill(color)
      display.flip()
