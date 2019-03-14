import os
import comtypes

# Requires pip3 install comtypes
# Tested with comtypes-1-17 

print("Beginning test of Microsoft Speech API")

# Using the Microsoft Speech API (SpVoice) 
# https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms723602(v%3Dvs.85)
from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
engine.speak("Hello World")