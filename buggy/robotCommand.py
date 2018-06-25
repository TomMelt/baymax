from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
from motor import moveF

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
    moveF(distance=ForwardNumber)
    go_msg= '...moving forward '+str(ForwardNumber)+' steps'+str(type(ForwardNumber))
    return question(go_msg)


@ask.intent("BackwardIntent",convert={"BackwardNumber":int})
def backward_intent(BackwardNumber):
    moveB(distance=BackwardNumber)
    go_msg= '...moving backward '+str(BackwardNumber)+' steps'+str(type(BackwardNumber))
    return question(go_msg)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return question(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
