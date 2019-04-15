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
from PIL import Image
from picamera import PiCamera
from time import sleep
import pygame


# def help_button_pressed():
#     if not buttons_setup_done:
#         print('First ensure that the buttons are properly setted-up.')
#         exit(1)
#     return GPIO.input(help_button_pin)
#
#
# def photo_button_pressed():
#     if not buttons_setup_done:
#         print('First ensure that the buttons are properly setted-up.')
#         exit(1)
#     return GPIO.input(photo_button_pin)


# def buttons_setup():
#     import RPi.GPIO as GPIO
#     global buttons_setup_done
#     buttons_setup_done = False
#     GPIO.setmode(GPIO.BOARD)
#     global help_button_pin
#     global photo_button_pin
#     help_button_pin = 16  # Edit accordingly to the circuit
#     photo_button_pin = 18  # Edit accordingly to the circuit
#     GPIO.setup(help_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(photo_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     buttons_setup_done = True


def capture_image(parameters):
    fullpath = parameters['path'] + parameters['ext']
    i = 0
    while os.path.exists(fullpath):
        fullpath = parameters['path'] + str(i) + parameters['ext']
        i += 1 
    camera = PiCamera()
    camera.resolution = parameters['resolution']
    camera.framerate = parameters['framerate']
    sleep(parameters['sleep_time'])
    camera.capture(fullpath)
    # im = Image.open(parameters['path'])
    return fullpath


def play_audio(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    # pygame.mixer.music.load('audio/help.ogg')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
