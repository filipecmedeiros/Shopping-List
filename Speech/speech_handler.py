from flask import Flask
from flask import request
from flask import render_template
import os
import requests
from Speech import Speech
import logging as log

def speech_handler():
    if request.method == "POST":
        audio = request.files['audio_data']
        speech = Speech('wav')
        text = speech.process(audio)
        log.warning(text)
        data = {'text': text}
        response = requests.post('http://app:8000/api/', json=data, verify=False)
        log.info(response)
        return render_template('index.html', request="POST")   
    else:
        return render_template("index.html")