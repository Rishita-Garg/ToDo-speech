import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Recognize speech

# Initialize text-to-speech engine
engine = pyttsx3.init()
tasks = []

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return "None"

def main():
    speak("Welcome to your To-Do List Assistant. What would you like to do?")
    while True:
        command = take_command()
        
        if "add" in command:
            task = command.replace("add", "").strip()
            tasks.append(task)
            speak(f"Task added: {task}")
        
        elif "show" in command or "view" in command:
            if tasks:
                speak("Your current tasks are:")
                for i, task in enumerate(tasks, 1):
                    speak(f"Task {i}: {task}")
            else:
                speak("Your to-do list is empty.")
        
        elif "remove" in command:
            speak("Which task would you like to remove?")
            task = take_command()
            if task in tasks:
                tasks.remove(task)
                speak(f"Task removed: {task}")
            else:
                speak("Task not found.")
        
        elif "stop" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I did not understand that. Please repeat.")

if __name__ == "__main__":
    main()
