#!/usr/bin/env python3

import time
from Xlib.display import Display
import os
from subprocess import Popen

def play_sound(file):
    Popen(['mplayer', file])

disp = Display()
empty_keys = [0] * 32
return_key = ([0] * 4) + [16] + ([0] * 27)
last_keys = [0] * 32

while 1:
    keys = disp.query_keymap()
    if keys != last_keys and keys != empty_keys:
        if keys == return_key:
            play_sound('return_sound.wav')
        else:
            play_sound('key_sound.wav')

    last_keys = keys
    time.sleep(0.05)
    
