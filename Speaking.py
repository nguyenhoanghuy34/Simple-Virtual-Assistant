import pyttsx3

robot_brain = "Thank you for using my service, dear guy !"
robot_mouth = pyttsx3.init()

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()