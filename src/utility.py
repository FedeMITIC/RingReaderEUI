"""
File: utility.py

Contains various utility functions:
- button_pressed(): detects if the user pressed a button connected to the PI
- button_setup(): sets up the button [see https://www.makeuseof.com/tag/add-button-raspberry-pi-project]
- capture_image(parameters): captures the image from the Pi Camera
- play_audio(path): loads the audio file stored in 'path' and plays it

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""
import os
from picamera import PiCamera
import pygame
import RPi.GPIO as GPIO
from time import sleep


def capture_image(parameters):
    fullpath = parameters['path'] + parameters['ext']
    i = 0
    while os.path.exists(fullpath):
        if i < parameters['max_image_stor']:
            i += 1
        else:
            i = 0
        fullpath = parameters['path'] + str(i) + parameters['ext']
    camera = PiCamera()
    camera.resolution = parameters['resolution']
    camera.framerate = parameters['framerate']
    sleep(parameters['sleep_time'])
    camera.capture(fullpath)
    return fullpath


def play_audio(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue