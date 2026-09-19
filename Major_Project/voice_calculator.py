"""
Speech Recognition : pip install SpeechRecognition 
pyttx3:Text to Speech
pyAudio
"""

import pyttsx3 


# import speech_recognition as sr 
# engine=pyttsx3.init()
# word='Hello World , how are you'
# engine.say(word )
# engine.runAndWait()

# recognizer=sr.Recognizer()

# with sr.Microphone() as source:
#     print("Adjusting for background noise... Please wait.")
#     recognizer.adjust_for_ambient_noise(source, duration=1)
#     print("Ready! Speak into the microphone...")

# while True:
#     with sr.Microphone() as source:
#         try:
#             print("\nListening...")
#             # listen() stops automatically after speech pauses
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

#             print("Recognizing...")
#             text = recognizer.recognize_google(audio)
#             print(f"You said: {text}")

#         except sr.WaitTimeoutError:
#             print("No speech detected, listening again...")
#         except sr.UnknownValueError:
#             print("Could not understand the audio. Please try speaking clearer.")
#         except sr.RequestError as e:
#             print(f"Network error from Google Speech Recognition service: {e}")
#         break 

# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

# print("Audio captured!")
# print("Audio length:", len(audio.frame_data))

# try:
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)

# except sr.UnknownValueError:
#     print("Google could not understand the audio.")

# except sr.RequestError as e:
#     print("Google request error:", e)

###################################################################################

# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = recognizer.listen(source, phrase_time_limit=5)

# print("Audio captured!")
# print("Audio length:", len(audio.frame_data))

# try:
#     text = recognizer.recognize_google(
#         audio,
#         language="en-US"
#     )

#     print("You said:", text)

# except sr.UnknownValueError:
#     print("Google could not understand the audio.")

# except sr.RequestError as e:
#     print("Google request error:", e)

#******************************* trying raw code ***********************************##
import speech_recognition as sr
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print(text)
        break 
