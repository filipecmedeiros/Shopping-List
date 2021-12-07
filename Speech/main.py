#!/usr/bin/env python
# -*- coding: utf-8 -*-
from AppModule import AppModule
from injector import Injector
from flask_injector import FlaskInjector
from speech_handler import speech_handler
import os


def start_server():
    print('start_server')
    app = AppModule.instance()
    flask_app = app.flask_app()
    
    flask_app.add_url_rule('/', 'index', speech_handler, methods=['GET', 'POST'])

    injector = Injector([app])
    FlaskInjector(app=flask_app, injector=injector)

    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    start_server()
