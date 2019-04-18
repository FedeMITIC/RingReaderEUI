#!/usr/bin/env python3
"""
File: detect_text.py

Open an image and detects the text inside it

Author:     Federico Macchi
Date:	    03/03/2019
Version     0.1.0
License:    MIT
"""
import io
from google.cloud import vision


def detect_document(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print(word_text, end=" ")
    return word_text

