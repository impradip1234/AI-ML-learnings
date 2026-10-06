import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)

print("Paste your text below. Press Enter twice to start speaking:")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

engine.say(text)
engine.runAndWait()