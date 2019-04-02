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
import base64
from utility import *
from detect_text import image_to_text
from time import sleep
from tts import text_to_speech
import os


def cleanup():
    # check if audio files still exists and remove them
    if os.path.exists(path=path + '.txt'):
        os.remove(path=path + '.txt')
    if os.path.exists(path=path + '.mp3'):
        os.remove(path=path + '.mp3')


def main():
    """
    Todo: set-up buttons and infinite loop
    """
    # passed_epoch = 1
    # while True:
    #     # passed_epoch gets incremented every time the user does not use the button.
    #     # it is then used to sleep the process (save resources) for a certain amount time that increase over time
    #     # at most it will become 12, meanin that 120seconds will be waited (2 mins)
    #     sleep(passed_epoch * 10)
    #     if button_pressed():
    #         passed_epoch = 0
    #         start()
    #     else:
    #         passed_epoch += 1
    #         if passed_epoch > 12:
    #             passed_epoch = 0
    #         pass
    start()


def prepare_audio_file(input_path, output_path):
    input_file = open(input_path, 'r')
    file_content = input_file.read()
    decoded_content = base64.b64decode(file_content)
    output_file = open(output_path, 'wb+')
    output_file.write(decoded_content)
    input_file.close()
    output_file.close()


def start():
    """
    Todo: clean the read text (especially escape quotation mark characters)
    """
    # Define the params to capture the image
    img_capture_params = {
        'framerate': 15,                # The framerate of the camera (15 is mandatory for the maximum resolution
        'path': 'hq.jpg',               # Path where the captured image will be stored
        'resolution': (2592, 1944),     # Resolution (tuple): resolution of the camera (2592, 1944) is the maximum
        'sleep_time': 3                 # Sleep time (in seconds) to let the sensor focus on the object
    }
    # Capture the image using the camera
    capture_image(parameters=img_capture_params)
    # Extract the text from the image
    text = image_to_text(api_key=API_KEY_OCR, path=img_capture_params['path'])
    # Transform the text into speech
    if text_to_speech(api_key=API_KET_TTS, text=text, path=path):
        # Play audio
        # play_audio(path=path)
        prepare_audio_file(input_path=path + '.txt', output_path=path + '.mp3')
        play_audio(path=path + '.mp3')
    else:
        print('API call didn\'t work')


def setup():
    # Get the API key
    try:
        file_ocr = open('../API_OCR.txt', 'r')
        file_tts = open('../API_TTS.txt', 'r')
        global API_KEY_OCR
        global API_KET_TTS
        API_KEY_OCR = file_ocr.read()
        API_KET_TTS = file_tts.read()
        file_ocr.close()
        file_tts.close()
    except FileNotFoundError:
        print('Impossible to load API Key')
        exit(1)
    global path
    # Tmp path to store the audio
    path = 'audio/tmp/output_test'


if __name__ == "__main__":
    setup()
    # play_audio('audio/help.ogg')  # Will be moved in the loop and played upon the pression of the help button
    main()
    cleanup()
