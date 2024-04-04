import pyttsx3          #voice to text
import speech_recognition as sr
import datetime

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
print(voices)

def speak(audio):                   #text to voice
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query
def wishingfun():                   #Wishing function which wish according to time
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("GOOD MORNING SIR")
    elif hour>12 and hour<=16:
        speak("GOOD AFTERNOON SIR")
    elif hour>16 and hour<=20:
        speak("GOOD EVENING SIR")
    else:
        speak("GOOD NIGHT SIR")
    speak("I AM ISHAAN SIR,HOW MAY I HELP YOU!!")

if __name__=='__main__':
    wishingfun()
    takecommand()