import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("Available voices:")
for idx, voice in enumerate(voices):
    print(f"{idx}: {voice.id} - {voice.name}")

engine.say("Testing voice")
engine.runAndWait()

