from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
from motor import moveF, moveB, moveL, moveR
from camera import picture

app = Flask(__name__)
ask = Ask(app, "/robot_commands")


@app.route('/')
def homepage():
    return "hi there, how ya doin?"


@ask.launch
def start_skill():
    welcome_message = 'Hey homies, I am the best robot'
    return question(welcome_message)


def moveD(direction, length):
    if direction[0].upper() == "F":
        moveF(distance=length)
        msg = 'moving forward '+str(length)+' steps'
    if direction[0].upper() == "B":
        moveL(angle=180)
        moveF(distance=length)
        moveR(angle=180)
        msg = 'moving backward '+str(length)+' steps'
    if direction[0].upper() == "R":
        moveR(angle=90)
        moveF(distance=length)
        msg = 'moving right '+str(length)+' steps'
    if direction[0].upper() == "L":
        moveL(angle=90)
        moveF(distance=length)
        msg = 'moving left '+str(length)+' steps'
    return msg


@ask.intent(
        "MoveIntent", convert={
            "direction":str,
            "length":int,
            "directiontwo":str,
            "lengthtwo":int,
            }
        )
def move_intent(direction, length, directiontwo, lengthtwo):
    if isinstance(direction+directiontwo, str) and isinstance(length+lengthtwo, int):
        msg1 = moveD(direction=direction, length=length)
        msg2 = moveD(direction=directiontwo, length=lengthtwo)
        return question(msg1+msg2)
    else:
        print([type(i) for i in [direction, length, directiontwo, lengthtwo]])
        return question("please try again.")


@ask.intent("ForwardIntent",convert={"ForwardNumber":int})
def forward_intent(ForwardNumber):
    if isinstance(ForwardNumber, int):
        if moveF(distance=ForwardNumber):
            go_msg= '...moving forward '+str(ForwardNumber)+' steps'
            return question(go_msg)
        else:
            go_msg= '...we are going to crash!'
            return question(go_msg)
    else:
        return question("please try again.")


@ask.intent("BackwardIntent",convert={"BackwardNumber":int})
def backward_intent(BackwardNumber):
    if isinstance(BackwardNumber, int):
        moveB(distance=BackwardNumber)
        go_msg= '...moving backward '+str(BackwardNumber)+' steps'
        return question(go_msg)
    else:
        return question("please try again.")


@ask.intent("RightIntent",convert={"RightNumber":int})
def right_intent(RightNumber):
    if isinstance(RightNumber, int):
        moveR(angle=RightNumber)
        go_msg= '...turning right '+str(RightNumber)+' degrees'
        return question(go_msg)
    else:
        return question("please try again.")


@ask.intent("LeftIntent",convert={"LeftNumber":int})
def left_intent(LeftNumber):
    if isinstance(LeftNumber, int):
        moveL(angle=LeftNumber)
        go_msg= '...turning left '+str(LeftNumber)+' degrees'
        return question(go_msg)
    else:
        return question("please try again.")


@ask.intent("DescribeSurrounding")
def self_intent():
    filename = picture()
    msg = 'I have taken a picture'
    return question(msg)


@ask.intent("SelfDestruct")
def self_intent():
    msg = 'Self Destruct... in 5... 4... 3... 2... 1... I dont wanna dieeeeeee. Overiding self destruct. phew that was a close one.'
    return question(msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return question(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
