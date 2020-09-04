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
import io
from google.cloud import texttospeech


def tts(text, path):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open(path, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file {}'.format(path))