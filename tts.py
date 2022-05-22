#https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python

import speech_recognition as sr
import requests
# Import the required module for text 
# to speech conversion
from gtts import gTTS 
# This module is imported so that we can 
# play the converted audio
import os

filename = "helloWorld.wav"

# initialize the recognizer
r = sr.Recognizer()
#initialize text variable
text = ''


# ------------------- SPEECH TO TEXT -------------------

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

# ------------------- TEXT TO DEEP AI -------------------


r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': text,
    },
    headers={'api-key': '4588448a-9284-4401-b3cb-552695a96edc'}
)
print(r.json())
json = r.json()
output = json.get('output')


# ------------------- TEXT TO SPEECH -------------------

# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=output, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")