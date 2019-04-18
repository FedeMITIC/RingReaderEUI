#!/usr/bin/env python3

"""
File: main.py

Entry point of the application:
- reads the API Key from a file external to the repo and saves it in the global variable API_KEY
- captures the image from the PiCamera
- extracts the text from the image
- transforms the text in speech
- plays the resulting audio file

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""
from utility import play_audio
from utility import capture_image
from detect_text import detect_document as detect_text
# from time import sleep
from tts import tts
# import os


# TODO: have a look at this https://stackoverflow.com/questions/16143842/raspberry-pi-gpio-events-in-python/18596063#18596063
# TODO: put configuration in a separate file https://docs.python.org/3.4/library/configparser.html
# TODO: sanitize read text https://stackoverflow.com/questions/2464959/whats-the-u-prefix-in-a-python-string


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
    play_audio(audio_path)


if __name__ == "__main__":
    start()