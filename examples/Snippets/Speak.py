import os

# Requires pip3 install comtypes
# Tested with comtypes-1-17 
# https://pypi.org/project/comtypes/
import comtypes

print("Beginning test of Microsoft Speech API")

# Using the Microsoft Speech API (SpVoice) 
# https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms723602(v%3Dvs.85)
from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
engine.speak("Hello World")



# using pyttsx3 - Offline text to speech for python3
# https://pythonprogramminglanguage.com/text-to-speech/
# https://pyttsx3.readthedocs.io/en/latest/
# https://github.com/nateshmbhat/pyttsx3
# 
# ****  error says that engine isn't found...?
# import pyttsx
# engine = pyttsx.init()
# engine.say("I will speak this text")
# engine.runAndWait()




# Using IBM Waton TTS 
# pip install tts-watson
#
# **** ERROR during install...
# 
# TBD...
# 




# Using Google Speech API
# https://pythonspot.com/speech-recognition-using-google-speech-api/comment-page-1/
#
# TBD...
# 



# Google Web to Speech (via Browser)
# https://www.google.com/intl/en/chrome/demos/speech.html
# 
# TBD...
# 


