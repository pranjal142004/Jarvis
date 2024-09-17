import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use voices[1] for female, voices[0] for male
engine.setProperty('rate', 150)

def speak(audio):
    print(f"Speaking: {audio}")
    engine.say(audio)
    engine.runAndWait()

def takeCommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1  # Adjust if needed
        audio = r.listen(source)
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again please.....")
        return "None"
    
    return query

if __name__ == "__main__":
    while True:
        query = takeCommond().lower()
        if 'jarvis' in query:
            print("Yes Boss") 
            speak("Yes Boss")
        else:
            speak("Please Speak again Boss")
