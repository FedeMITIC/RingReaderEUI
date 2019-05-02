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
from utility import play_audio
from utility import capture_image
from detect_text import detect_text
from time import sleep
import RPi.GPIO as GPIO
from tts import tts
# import os


# TODO: have a look at this https://stackoverflow.com/questions/16143842/raspberry-pi-gpio-events-in-python/18596063#18596063
# TODO: put configuration in a separate file https://docs.python.org/3.4/library/configparser.html
# TODO: sanitize read text https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string


# def setup(path):
#     import configparser
#     conf_path = path
#     if path == '':
#         conf_path = 'conf.ini'
#     config = configparser.ConfigParser()
#     config.read(conf_path)
#     conf = dict()
#     for key in config.sections():
#         print(key)
def my_callback(channel):
    sleep(1)
    if GPIO.input(15):
        # start()
        print('Start pressed')
    if GPIO.input(24):
        print('Help pressed')
        play_audio('audio/help.ogg')


def start():
    """
    Todo: clean the read text (especially escape quotation mark characters)
    """
    # Define the params to capture the image
    img_capture_params = {
        'framerate': 15,                     # The framerate of the camera (15 is mandatory for the maximum resolution)
        'path': 'test_imgs/tmp',  # Path where the captured image will be stored
        'ext': '.jpg',
        'resolution': (2592, 1944),          # Resolution (tuple): resolution of the camera (2592, 1944) is the maximum
        'sleep_time': 3                      # Sleep time (in seconds) to let the sensor focus on the object
    }
    # play_audio('audio/help.ogg')  # Will be moved in the loop and played upon the pression of the help button
    audio_path = 'audio/tmp/output.mp3'
    # Capture the image using the camera
    captured_image_path = capture_image(parameters=img_capture_params)
    # Extract the text from the image
    text = detect_text(path=captured_image_path)
    # Transform the text into speech
    tts(text=text, path=audio_path)
    # Play audio
    play_audio(path=audio_path)


if __name__ == "__main__":
    # To allow overriding the default configuration; the arguments must be a valid path
    # conf is a dictionary where the keys are configuration options and the values are the values of those configurations
    # conf = setup(sys.argv[1])
    # start(configuration=conf)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(15, GPIO.RISING, callback=my_callback, bouncetime=300)
    GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=300)
    while True:
        pass
