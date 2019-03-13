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

import requests


def text_to_speech(api_key, text):
    # Append the API Key to the endpoint to authenticate with the APIs
    endpoint = 'https://texttospeech.googleapis.com/v1/text:synthesize?key=' + str(api_key)
    print(endpoint)
    # API call
    # with open('output.ogg', 'wb') as out:
    #    out.write(response.audio_content)
    #    print('Audio content written to file "output.mp3"')


if __name__ == '__main__':
    print('DEBUG')
    text = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, " \
           "thank you very much. They were the last people you'd expect to be involved in anything strange or " \
           "mysterious, because they just didn't hold with such nonsense. Mr. Dursley was the director of a firm " \
           "called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a " \
           "very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, " \
           "which came in very useful as she spent so much of her time craning over garden fences, spying on the  " \
           "neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy " \
           "anywhere. The Dursleys had everything they wanted, but they also had a secret, and their greatest fear " \
           "was that somebody would discover it. They didn't think they could bear it if anyone found out about the " \
           "Potters. Mrs. Potter was Mrs. Dursley's sister, but they hadn't met for several years; in fact, " \
           "Mrs. Dursley pretended she didn't have a sister, because her sister and her good-for-nothing husband were " \
           "as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if " \
           "the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had " \
           "never even seen him. This boy was another good reason for keeping the Potters away; they didn't want " \
           "Dudley mixing with a child like that. "
    text_to_speech(api_key=open('../API.txt', 'r').read(), text='daw')
