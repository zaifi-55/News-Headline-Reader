import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.say("Hello Huzaifa, this is a test of the text to speech engine")
engine.runAndWait()