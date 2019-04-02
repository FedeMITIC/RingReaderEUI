#!/usr/bin/env python3
"""
File: detect_text.py

Open an image and detects the text inside it

Author:     Federico Macchi
Date:	    03/03/2019
Version     0.1.0
License:    MIT
"""
import sys
from api import *
import json


def image_to_text(api_key, path):
    # try:
    #     image = get_image(path)
    # except FileNotFoundError:
    #     print("Impossible to load {}, file not found.".format(path))
    text_from_image = ""
    endpoint = 'https://vision.googleapis.com/v1/images:annotate?key=' + api_key
    try:
        text_from_image = detect_text_api(endpoint=endpoint, data_to_send=path)
    except APIError:
        exit(API_ERROR_INVALID_FORMAT)
    print("Detected text: {}".format(text_from_image))
    # This is just terrible.
    text = json.loads(text_from_image, encoding='utf-8')
    text = text['responses']
    return text[0]['textAnnotations'][0]['description']
    # Process the extracted text

