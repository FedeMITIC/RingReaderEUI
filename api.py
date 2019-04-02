"""
File: api.py

Contains the functions necessary to fire the API calls.
The API specs are defined in tts.py file.

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""
import requests
import base64


# Error codes + MACROS
API_ERROR_INVALID_KEY = 2
API_ERROR_INVALID_FORMAT = 3
API_RESPONSE_OK = 200
API_RESPONSE_UNAUTHORIZED = 401
API_RESPONSE_FORBIDDEN = 403


# Defines a custom Exception wrapper
class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: Google Cloud Vision API replied with code: {}".format(self.status)


def detect_text_api(endpoint, data_to_send):
    """
    detect_text: query the remote API to detect and extract the text from the image
    :param endpoint: the API endpoint
        :type: string
    :param data_to_send: the PATH of the image to convert to base64 and send
        :type: string
    :return: the extracted text
        :type: string

    cURL request example
    curl -X POST -H "Content-Type: application/json; charset=utf-8" --data "{'requests': [{'image': {'source': {'imageUri': 'gs://bucket-name-123/abbey_road.jpg'}},'features': [{'type': 'TEXT_DETECTION'}]}]}" "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCaIGDVt1dla0V0U19Dv3IOnBCG5FCAE9E"
    """
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }
    # data using a Base64 image
    data = '{"requests":[{"image":{"content":"' + encode_image(data_to_send).decode('utf-8') + '"},"features":[{"type":"DOCUMENT_TEXT_DETECTION"}]}]}'
    # data using a URL
    # data = "{'requests': [{'image': {'source': {'imageUri': 'gs://bucket-name-123/abbey_road.jpg'}},'features':[{" \
    #      "'type': 'TEXT_DETECTION'}]}]} "
    request = requests.Request(
        'POST',
        endpoint,
        headers=headers,
        data=data
    )
    ready = request.prepare()
    # Pretty print the request BEFORE sending it out
    pretty_print_post(ready)
    # Send the request
    """
    Disclaimer: please send the request ONLY if the printed version obtained from above is correct,
    to avoid wasting API calls.
    """
    session = requests.Session()
    response = session.send(ready)
    print(response)
    if response.status_code == API_RESPONSE_OK:
        return response.text
    else:
        raise APIError(response.status_code)
    # return 'Debug - No API call sent'
    # # Instead of calling the API, to avoid consuming API quota do a fake call and load the fake reply from a file
    # return open('response.txt', 'r').read()


def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read())


def pretty_print_post(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
        '------------END------------'
    ))


def synthesize_text_api(endpoint, data_to_send):
    """
        synthesize_text: query the remote API to transform the text into speech
        :param endpoint: the remote API endpoint
            :type: string
        :param data_to_send: the text to be syntesized
            :type: string
        :return:
            :type: True if successfull, False otherwise
    """
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }
    # Prepare the data for the request
    data = '{"audioConfig":{"audioEncoding":"MP3","effectsProfileId":["small-bluetooth-speaker-class-device"],"pitch":"0.00","speakingRate":"1.00"},"input":{"text":"' + str(data_to_send) + '"},"voice":{"languageCode":"en-US","name":"en-US-Wavenet-E"}}'
    # data = "{'input':{'text':'" + str(data_to_send) + "'},'voice':{'languageCode':'en-gb','name':'en-GB-Standard-A','ssmlGender':'FEMALE'},'audioConfig':{'audioEncoding':'MP3'}}"
    # data = "{'input':{'text':'" + data_to_send + "'},'voice':{'languageCode':'en-gb','name':'en-GB-Standard-A','ssmlGender':'FEMALE'},'audioConfig':{'audioEncoding':'MP3'}}"
    # data = data.encode('utf-8')
    request = requests.Request(
        'POST',
        endpoint,
        headers=headers,
        data=data
    )
    ready = request.prepare()
    # Pretty print the request BEFORE sending it out
    pretty_print_post(ready)
    # Send the request
    """
    Disclaimer: please don't waste API calls. Maximum 4.000.000 chars/month
    """
    session = requests.Session()
    response = session.send(ready)
    if response.status_code == API_RESPONSE_OK:
        return response.text
    else:
        raise APIError(response.status_code)
