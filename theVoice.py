
#https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
#https://classes.engineering.wustl.edu/ese205/core/index.php?title=Audio_Input_and_Output_from_USB_Microphone_%2B_Raspberry_Pi

import speech_recognition as sr
import requests
# Import the required module for text 
# to speech conversion
from gtts import gTTS 
# This module is imported so that we can 
# play the converted audio
import os

#GPIO/Pi dependcies 
#from gpiozero import Device, LED, Button                                                 # (1)
#from gpiozero.pins.pigpio import PiGPIOFactory
#import signal     

import random
import time
import wave
import io
import requests

from gpiozero import Device, LED, Button
from gpiozero.pins.pigpio import PiGPIOFactory
import signal


#intializing pin numbers
LED_GPIO_PIN = 21
BUTTON_GPIO_PIN = 23

Device.pin_factory = PiGPIOFactory() #set gpiozero to use pigpio by default.

filename = "helloWorld.wav"

# initialize the recognizer
r = sr.Recognizer()
#initialize text variable
text = ''

led = LED(LED_GPIO_PIN)
button = Button(BUTTON_GPIO_PIN, pull_up=True, bounce_time=0.1) # Bounce time in seconds 

requestsSent = 0

makingList = ["the conduct of thought goes along with, and continually answers to, the fluxes and flows of the materials within we work", 
"If the mind wants to be involved in the process of making it must not only be open, but forward looking, in the direction of as of yet unknown”. This is a matter not of predetermining the final forms of things and all the steps needed to get there, but of opening up a path and improvising a passage", 
"Though we may occupy a world of objects, to the occupant the contents of the world appear already locked into their final forms, as though they had turned their backs on us. To inhabit the world, by contrast, is to join in the process of formation. It is to participate in a dynamic world full of energies, forces and flows",
"To correspond with the world, in short, is not to describe it, or to represent it, but to answer to it",
"Know for yourself!",
"In the academic pantheon, reason is predestined to trump intuition, expertise to trump common sense, and conclusions based on the facts to trump what people know from ordinary experience or from the wisdom of their forebears",
" I have explained that it is wrong to think of learning as the transmission  of a ready-made body of information, prior to its application  in particular contexts of practice. On the contrary, we learn by doing , in the course of carrying out the tasks of life.",
"The drinks can: that’s aluminum; feel how light it is! The cigarette butt: well there is still some tobacco inside. Light it, and it will exude smoke, and the smoke makes trails in the air that bend this way and that in response to the fluxes and rhythms of our own breathing. The ball: that’s made of rubber, and by applying pressure with the hands, we can feel its softness and springiness. We could even put it between our teeth and imagine what it feels like to be a dog",
"think of making, instead, as a process of growth . This is to place the maker from the outset as a participant in amongst a world of active materials. These materials are what he has to work with, and in the process of making he ‘joins forces’ with them, bringing them together or splitting them apart, synthesizing and distilling, in anticipation of what might emerge.",
"there seem to be two sides to materiality. On one side is the raw physicality of the world’s ‘material character’; on the other side is the socially and historically situated agency of human beings who, in appropriating this physicality for their purposes, are alleged to project upon it both design and meaning in the conversion of naturally given raw material into the finished forms of artifacts",
"To describe any material is to pose a riddle, whose answer can be discovered only through observation and engagement with what is there. 3  The riddle gives the material a voice and allows it to tell its own story: it is up to us, then, to listen, and from the clues it offers, to discover what is speaking."]


def pauseRequests():
    time.sleep(3600)

def pressed():
    requestsSent =+ 1    
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
    time.sleep(.3)
    led.on()
    time.sleep(.3)
    led.off()
  
    if requestsSent >= 60: #to not hit the google tts cap 
        requestsSent = 0
        tooManyReqStr = "You have gained maximum insight from the Head. Pausing interactions. Please do not speak to the head for one hour to allow its wisdom to recharge. Thank you."
        tooManyReq = gTTS(text=tooManyReqStr, lang=language, slow=False)
        tooManyReq.save("tooManyRequests.wav")
        os.system("mpg123 tooManyRequests.wav")
        pauseRequests()

    else:                   #recieve and interpret mic input 
        with sr.Microphone() as source:
        # read the audio data from the default microphone
            led.on()
            print("Listening...")
            mic_audio_data = r.record(source, duration=8)
    
        print("Recognizing...")
        led.off()
        # convert speech to text
        micText = r.recognize_google(mic_audio_data)
        print(micText)

        if "making" or "Making" in micText: #making easter egg
           
            makingQuote = random.choice(makingList)
            language = 'en'
            myMaking = gTTS(text=makingQuote, lang=language, slow=False)
            myMaking.save("makingOutput.wav")
            os.system("mpg123 makingOutput.wav") 
        
        elif "Simon" or "Rush Limbaugh" or "Christine" or "Topher" or "Robot": #easter egg prompt
            os.system("mpg123 screaming.mp3") 
        
        else:
            # ------------------- TEXT TO DEEP AI -------------------

            rp = requests.post(
                "https://api.deepai.org/api/text-generator",
                data={
                    'text': micText,
                },
                headers={'api-key': '4588448a-9284-4401-b3cb-552695a96edc'}
            )
            print(rp.json())
            json = rp.json()
            micOutput = json.get('output')


            # ------------------- TEXT TO SPEECH -------------------

            # Language in which you want to convert
            language = 'en'
            
            # Passing the text and language to the engine, 
            # here we have marked slow=False. Which tells 
            # the module that the converted audio should 
            # have a high speed
            myobj = gTTS(text=micOutput, lang=language, slow=False)
            
            # Saving the converted audio in a mp3 file named
            # welcome 
            myobj.save("micOutput.wav")
            
            # Playing the converted file
            os.system("mpg123 micOutput.wav")

button.when_pressed = pressed                                                                         

signal.pause()    


   





                                                    



