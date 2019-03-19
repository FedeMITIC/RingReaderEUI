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


def detect_text(api_key, path):
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
    # Process the extracted text


# Used only to test if the API works, will be removed.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify an image file to load.")
        exit(1)
    print('DEBUG')
    detect_text(api_key=open('../API.txt', 'r').read(), path=sys.argv[1])
