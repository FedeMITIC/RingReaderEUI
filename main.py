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

from utility import *
# from detect_text import image_to_text
from tts import text_to_speech


def main():
    # while True:
    #     if button_pressed():
    #         start()
    #     else:
    #         pass
    start()


def start():
    # Define the params to capture the image
    params = []
    # Capture the image using the camera
    image = capture_image(parameters=params)
    # Extract the text from the image
    # text = image_to_text(API_KEY, image)
    text = 'Some random text that will be read aloud from the Raspberry Pi\'s speakers'
    # Transform the text into speech
    audio = text_to_speech(api_key=API_KEY, text=text)
    # Play audio
    audio_path = 'audio.ogg'
    play_audio(path=audio_path)


def setup():
    # Get the API key
    try:
        f = open('../API.txt', 'r')
        global API_KEY
        API_KEY = f.read()
        f.close()
    except FileNotFoundError:
        print('Impossible to load API Key')
        exit(1)


if __name__ == "__main__":
    setup()
    main()
