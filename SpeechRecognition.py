import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Function to capture voice input and convert to text
def convert_voice_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError as e:
        print(f"Error: {e}")

# Call the function to convert voice to text
voice_text = convert_voice_to_text()
print(f"You said: {voice_text}")
