#!/usr/bin/env python3

"""
File: detect_color.py

free API key for OCRAPI: a22a40442388957

Open an image and detects the colors inside it

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""

import base64
import numpy as np
import os
from PIL import Image
import time
import sys
import webcolors
import requests


# Courtesy of /users/1175101/fraxel from StackOverflow [https://stackoverflow.com/a/9694246]
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


# Courtesy of /users/1175101/fraxel from StackOverflow [https://stackoverflow.com/a/9694246]
def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def calculate_main_color(im):
    """
    Given an image, extract the RGB value of every pixel and calculates the "averageness" of R, G and B.

    :param im: The image
    :return: Bi-dimensional array of shape (1, 3); the columns represent the RGB color scheme
    """
    pixel = list(im.getdata())
    n_of_pixel = len(pixel)
    x_vec = np.zeros((1, 3))

    for j in range(n_of_pixel):
        x_vec[0, 0] += pixel[j][0]
        x_vec[0, 1] += pixel[j][1]
        x_vec[0, 2] += pixel[j][2]
    x_vec[0, 0] = int(x_vec[0, 0] / n_of_pixel)
    x_vec[0, 1] = int(x_vec[0, 1] / n_of_pixel)
    x_vec[0, 2] = int(x_vec[0, 2] / n_of_pixel)
    print(x_vec)
    return x_vec


def resize(img, basewidth):
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    return img.resize((basewidth, hsize), Image.ANTIALIAS)


def start(path):
    try:
        im = Image.open(path)
        orig_im = im
    except FileNotFoundError:
        print("Impossible to load {}, file not found.".format(path))
    width, height = im.size
    print('Original size ({}, {})'.format(width, height))
    # Resize the image
    im = resize(im, 300)
    width, height = im.size
    print('New size ({}, {})'.format(width, height))
    # Save the resized image
    im.save(path + '.thumbnail', "JPEG")
    # Convert the image to RGB
    rgb_im = im.convert('RGB')
    main_color = calculate_main_color(rgb_im)
    print("The dominant color in the image is R: {}, G: {}, B: {}".format(main_color[0, 0], main_color[0, 1],
                                                                          main_color[0, 2]))
    actual_name, closest_name = get_colour_name(tuple(main_color[0]))
    if actual_name is None:
        print("The closest color to RGB({}, {}, {}) is: {}".format(main_color[0, 0], main_color[0, 1],
                                                                   main_color[0, 2], closest_name))
    else:
        print("RGB({}, {}, {}) corresponds to {}".format(main_color[0, 0], main_color[0, 1],
                                                         main_color[0, 2], actual_name))

    with open(path + '.thumbnail', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    img_filetype = path.split('.')[1]
    img_filetype = 'image/' + img_filetype
    encoded_string = 'data:' + img_filetype + ';base64,' + encoded_string.decode("utf-8")
    print(img_filetype)
    url = 'https://api.ocr.space/parse/image'
    payload = {'language': 'eng',
               'isOverlayRequired': 'false',
               'base64image': encoded_string,
               'filetype': img_filetype,
               'iscreatesearchablepdf': 'false',
               'issearchablepdfhidetextlayer': 'false',
               'scale': 'true',
               'detectOrientation': 'true'}
    files = {}
    headers = {
        'apikey': 'a22a40442388957'
    }
    response = requests.post(
        url=url,
        headers=headers,
        data=payload,
        files=files,
        allow_redirects=False
    )
    print(response.text)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify an image file to load.")
        exit(1)
    start(sys.argv[1])
