import pyttsx3

robot_brain = "Chào Phúc Lý"

engine = pyttsx3.init()
engine.say(robot_brain)
engine.runAndWait()