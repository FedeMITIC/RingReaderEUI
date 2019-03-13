"""
File: tts.py

Calls the Google Cloud API and retrieve the audio files containing the spoken text.

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""

import requests


def text_to_speech(api_key, text):
    print('Text to speech')
