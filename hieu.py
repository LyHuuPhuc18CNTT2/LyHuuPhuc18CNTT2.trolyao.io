you = "hello"

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "today":
    robot_brain = "Thu 3"
elif you == "hello":
    robot_brain = "Hello Phuc Ly"
else:
    robot_brain = "I'm fine thank you, and you?"
print(robot_brain)