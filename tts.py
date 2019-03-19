"""
File: tts.py

Calls the Google Cloud API and retrieve the audio files containing the spoken text.
Docs: https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize
Demo page: https://cloud.google.com/text-to-speech/
Check voices and requests in the demo page.

POST https://texttospeech.googleapis.com/v1/text:synthesize

JSON representation of the BODY of the API call

{
  "input": {
      // Union field input_source can be only one of the following:
        "text": string,
        "ssml": string
      // End of list of possible types for union field input_source
  },
  "voice": {
        "languageCode": string,
        "name": string,
        "ssmlGender": 'SSML_VOICE_GENDER_UNSPECIFIED' OR 'MALE' OR 'FEMALE' OR 'NEUTRAL'
  },
  "audioConfig": {
        "audioEncoding": 'LINEAR16' OR 'MP3' OR 'OGG_OPUS',
        "speakingRate": number,
        "pitch": number,
        "volumeGainDb": number,
        "sampleRateHertz": number,
        "effectsProfileId": [
            string
        ]
  }
}

Author:     Federico Macchi
Date:	    26/02/2019
Version     0.1.0
License:    MIT
"""
from api import *


def text_to_speech(api_key, text, path):
    # Append the API Key to the endpoint to authenticate with the APIs
    endpoint = 'https://texttospeech.googleapis.com/v1/text:synthesize?key=' + str(api_key)
    result = False
    try:
        result = synthesize_text_api(endpoint=endpoint, data_to_send=text, file_path=path)
    except APIError:
        print('API call failed.')
        result = False
    return result


# Used only to test if the API works, will be removed.
if __name__ == '__main__':
    print('DEBUG')
    text = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, " \
           "thank you very much. They were the last people you'd expect to be involved in anything strange or " \
           "mysterious, because they just didn't hold with such nonsense."
    text_to_speech(api_key=open('../API.txt', 'r').read(), text=text, path='output.ogg')
