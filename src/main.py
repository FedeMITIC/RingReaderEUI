#!/usr/bin/env python3

"""
File: main.py

Entry point of the application:
- captures the image from the PiCamera
- extracts the text from the image
- transforms the text in speech
- plays the resulting audio file

Author:     Federico Macchi
Date:	    19/04/2019
Version     1.0.0
License:    MIT


DISCLAIMER: setup the service account using this guide https://cloud.google.com/vision/docs/quickstart-client-libraries
before usage.
"""
from utility import *
from detect_text import detect_text
from time import sleep
import RPi.GPIO as GPIO
from tts import tts


def start_button_pressed_callback(e):
    print("Callback 1 called")
    sleep(1)
    if GPIO.input(15):
        print('Start pressed')
        start()


def help_button_pressed_callback(e):
    print("Callback 2 called")
    sleep(1)
    if GPIO.input(24):
        print('Help pressed')
        play_audio('audio/help.ogg')


def start():
    # Define the params to capture the image
    img_capture_params = {
        'framerate': 15,                     # The framerate of the camera (15 is mandatory for the maximum resolution)
        'path': 'test_imgs/tmp',             # Path where the captured image will be stored
        'ext': '.jpg',                       # Image extension
        'resolution': (2592, 1944),          # Resolution (tuple): resolution of the camera (2592, 1944) is the maximum
        'sleep_time': 3,                     # Sleep time (in seconds) to let the sensor focus on the object
        'max_image_stor': 20                 # Maximum amount of image to be stored
    }
    audio_params = {
        'path': 'audio/tmp/output.mp3',
        'ext': '.mp3',
        'sound_end_page': 'audio/end_page.ogg'
    }
    # Capture the image using the camera
    print("Capturing the image...")
    captured_image_path = capture_image(parameters=img_capture_params)
    # Extract the text from the image
    print("Detecting text...")
    text = detect_text(path=captured_image_path)
    # Transform the text into speech
    print("Generating speech...")
    tts(text=text, path=audio_params['path'])
    # Play audio
    print("Playing audio...")
    play_audio(path=audio_params['path'])
    print("Page ended")
    play_audio(path=audio_params['sound_end_page'])


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(15, GPIO.FALLING, callback=start_button_pressed_callback, bouncetime=300)
    GPIO.add_event_detect(24, GPIO.FALLING, callback=help_button_pressed_callback, bouncetime=300)
    print("Setup complete")
    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()