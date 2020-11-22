#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template
from jinja2 import Template


# Support for 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()