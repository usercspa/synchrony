import os
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

# Support for 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
pyperclip.copy('link')

#get timezone
response = requests.get("http://api.timezonedb.com/v2.1/list-time-zone?key=16OLECLBWBT9&format=json")
zones = response.json()["zones"]
for z in zones:
    print(z["zoneName"])