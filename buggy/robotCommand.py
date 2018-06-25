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

@ask.intent("ForwardIntent")
def forward_intent(ForwardNumber):
    moveF()
    go_msg= 'The sky is the limit, moving forward much'
    return statement(go_msg)


@ask.intent("BackwardIntent",convert={"BackwardNumber":int})
def backward_intent(BackwardNumber):
    go_msg= 'I am not a coward but moving forward {}'.format(BackwardNumber)
    return statement(go_msg)




@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)
    
if __name__ == '__main__':
    app.run(debug=True)
