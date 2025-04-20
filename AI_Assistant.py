import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()
robot_brain=""

while True:
    # Listening
    with speech_recognition.Microphone() as mic:
        print("Robot: I am Listening")
        audio = robot_ear.listen(mic)
    print("Robot:.......")
    try:
        you = robot_ear.recognize_google(audio)
        print("Your Question: "+ you)
    except speech_recognition.UnknownValueError:
        print("Robot: Sorry, I did not understand.")
    except speech_recognition.RequestError:
        print("Robot: Could not request results, please check your internet.")
    except:
        you = ""


    #Understanding
    if you == "":
        robot_brain = "I can't hear you, try again !"
    elif  "hello" in you:
        robot_brain = "Hello guy, Nguyen Hoang Huy !"
    elif "thank you" in you:
        robot_brain = "Thank you for using my service, dear guy !"
    elif "today" in you:
        now = date.today()
        date_string = now.strftime("Today is %d %m %Y")
        robot_brain = date_string
    elif  "time" in you:
        now = datetime.now()
        time_string = now.strftime("Now is %H hours %M minutes %S seconds")
        robot_brain = time_string
    elif "bye" in you:
        robot_brain = "See you later, Nguyen Hoang Huy !"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else: 
        robot_brain = "Thanks a lot"
    print ("Robot Answer: "+robot_brain)


    #Speaking
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
