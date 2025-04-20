import speech_recognition

robot_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("Robot: I am Listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
    print(you)
except speech_recognition.UnknownValueError:
    print("Robot: Sorry, I did not understand.")
except speech_recognition.RequestError:
    print("Robot: Could not request results, please check your internet.")
