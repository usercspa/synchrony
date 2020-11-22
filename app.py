import requests
import configparser
from flask import Flask, render_template, request
import pyperclip
app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('index.html')

pyperclip.copy('link')

if __name__ == '__main__':
    app.run()

