import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialization Section
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def listener():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You Said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that. Say it again loudly.")
        return None
    
def Do(command):
    
    if "youtube" in command:
        speak("what you want to search on youtube?")
        print("what you want to search on youtube?")
        topic = listener()
        if topic:
            print(f"Opening youtube for {topic}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")
        
    elif "github" in command:
        print("Opening Github...")
        webbrowser.open("https://github.com")
        
    elif "facebook" in command:
        print("Opening facebook...")
        webbrowser.open("https://www.facebook.com")
        
    elif "search" in command:
        print("What you want to search ?")
        user_want = listener()
        if user_want:
            speak("what you want to search on Google?")
        webbrowser.open(f"https://www.google.com/search?q={user_want}")
            
    elif "hackerrank" in command:
        print("Opening Hackerrank...")
        webbrowser.open("https://www.hackerrank.com")
    elif "chat gpt" in command:
        print("Opening ChatGPT.")
        webbrowser.open("https://www.chatgpt.com")
        
    elif "exit" in command:
        print("Exiting program.")
        return False
    
    
    return True


if __name__ == "__main__":
    command = listener()
    if "venom" in command:
        print("Yes Sir...")
        while True:
            print("Listening...")
            command = listener()
            if command:
                if not Do(command):
                    break
