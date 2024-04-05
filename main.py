import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
import pygame
import os
# Chatgpt API KEY -- Your_own API Key
def play_audio(file_path):
    # Initialize Pygame mixer
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error:
        say("Couldn't play the song , sorry boss.")

    pygame.mixer.quit()

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(text)

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        baat = recognizer.recognize_google(audio)
        print(f"User said: {baat}")
        return baat.lower()
    except sr.UnknownValueError:
        return "SPEECH NOT RECOGNISED"
    except sr.RequestError as e:
        say(f"Error during speech recognition: {e}")
        return "SPEECH NOT RECOGNISED"

def ai_command():
    openai.api_key = 'Your_own API Key'  
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": baat}])
    return(response['choices'][0]['message']['content'])
      
if _name_ == "_main_":
    print('HAR HAR MAHADEV')
    say("hi boss i am your project.")

    while True:
        print("Listening...")
        baat = take_command()

        if "open" in baat and any(site in baat for site in
                                   ['youtube', 'google', 'wikipedia', 'instagram', 'chatgpt', 'spotify',
                                    'geeks for geeks']):
            site_name = next(site for site in
                             ['youtube', 'google', 'wikipedia', 'instagram', 'chatgpt', 'spotify', 'geeks for geeks'] if
                             site in baat)
            say(f"boss i am opening {site_name} for you.")
            webbrowser.open(f"https://{site_name}.com")

        elif "time kya hua hai" in baat:
            hour = datetime.datetime.now().strftime("%H")
            mn = datetime.datetime.now().strftime("%M")
            say(f"boss the time is {hour} and {mn} minutes")
            

        elif "chatbot" in baat:
            chatgpt_response =ai_command()
            print(chatgpt_response)
            say(chatgpt_response)
            

        elif "what are you doing" in baat:
            say("nothing boss just waiting for your command")

        elif "play music" in baat:
            say("playing music for you boss.... ")
            play_audio(r"C:\Users\sankh\Music\Pehle Bhi Main Animal 128 Kbps.mp3")
             
        if "exit" in baat.lower():
            say("thanks for using, have a good day")
            break
        else:
            say("anything else for me boss")
