from flask import Flask
from flask_ask import Ask, statement, question, session,convert_errors
import json
import requests
import time
import unidecode
from motor import moveF, moveB, moveL, moveR

app = Flask(__name__)
ask = Ask(app, "/robot_commands")


@app.route('/')
def homepage():
    return "hi there, how ya doin?"


@ask.launch
def start_skill():
    welcome_message = 'Hey homies, I am the best robot'
    return question(welcome_message)


@ask.intent("ForwardIntent",convert={"ForwardNumber":int})
def forward_intent(ForwardNumber):
    if "ForwardNumber" in convert_errors:
    	return question("did not understand the answer please repeat")
    else:
        if moveF(distance=ForwardNumber):
            go_msg= '...moving forward '+str(ForwardNumber)+' steps'
            return question(go_msg)
        else:
            go_msg= '...we are going to crash!'
            return question(go_msg)


@ask.intent("BackwardIntent",convert={"BackwardNumber":int})
def backward_intent(BackwardNumber):
    if "BackwardNumber" in convert_errors:
        return question("did not understand the answer please repeat")
    else:
        moveB(distance=BackwardNumber)
        go_msg= '...moving backward '+str(BackwardNumber)+' steps'
        return question(go_msg)


@ask.intent("RightIntent",convert={"RightNumber":int})
def right_intent(RightNumber):
    if "RightNumber" in convert_errors :
        return question("did not understand the answer please repeat")
    else:
        moveR(angle=RightNumber)
        go_msg= '...turning right '+str(RightNumber)+' degrees'
        return question(go_msg)


@ask.intent("LeftIntent",convert={"LeftNumber":int})
def left_intent(LeftNumber):
    if "LeftNumber" in convert_errors:
        return question("did not understand the answer please repeat")
    else:
        moveL(angle=LeftNumber)
        go_msg= '...turning left '+str(LeftNumber)+' degrees'
        return question(go_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return question(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
