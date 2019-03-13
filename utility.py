"""
File: utility.py

Contains various utility functions:
- button_pressed(): detects if the user pressed a button connected to the PI
- capture_image(parameters): captures the image from the Pi Camera
- play_audio(path): loads the audio file stored in 'path' and plays it

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""
import pygame


def button_pressed():
    return True


def capture_image(parameters):
    print(parameters)
    return None


def play_audio(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

