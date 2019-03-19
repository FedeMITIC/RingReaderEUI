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
import pygame
import RPi.GPIO as GPIO


def button_pressed():
    # if not is_button_setup:
    #    print('First ensure that the button is properly setted-up.')
    #    exit(1)
    return GPIO.input(button_pin)


def button_setup():
    global is_button_setup
    is_button_setup = False
    GPIO.setmode(GPIO.BOARD)
    global button_pin
    button_pin = 16
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    is_button_setup = True


def capture_image(parameters):
    print(parameters)
    return None


def play_audio(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

