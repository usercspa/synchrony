import os
import requests
from flask import Flask, render_template, request
from jinja2 import Template, Environment, FileSystemLoader, PackageLoader, select_autoescape
from firebase import firebase

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

#get timezone
response = requests.get("http://api.timezonedb.com/v2.1/list-time-zone?key=16OLECLBWBT9&format=json")
zones = response.json()["zones"]
for z in zones:
    print(z["zoneName"])
    
  
# configure Jinja to load templates 
env = Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def autoescape(template_name):
    if template_name is None:
        return False
    if template_name.endswith(('.html', '.htm', '.xml'))
    
  # load function

def load_template(name):
      if name == 'index.html':
       return '...'
loader = FunctionLoader(load_template)

#copy link
pyperclip.copy('link')

# find the best tme
response = requests.get("http://api.cronofy.com/v1/availability")
availability = response.json()["availability"]
for a in availability :
    print(a["bestTime"])
    
    
#python-firebase authentication
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', authentication=None)
result = firebase.get('/users', None, {'print': 'pretty'})
print result
{'error': 'Permission denied.'}

authentication = firebase.Authentication('THIS_IS_MY_SECRET', 'ozgurvt@gmail.com', extra={'id': 123})
firebase.authentication = authentication
print authentication.extra
{'admin': False, 'debug': False, 'email': 'ozgurvt@gmail.com', 'id': 123, 'provider': 'password'}

user = authentication.get_user()
print user.firebase_auth_token
"eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJhZG1pbiI6IGZhbHNlLCAiZGVidWciOiBmYWxzZSwgIml
hdCI6IDEzNjE5NTAxNzQsICJkIjogeyJkZWJ1ZyI6IGZhbHNlLCAiYWRtaW4iOiBmYWxzZSwgInByb3ZpZGVyIjog
InBhc3N3b3JkIiwgImlkIjogNSwgImVtYWlsIjogIm96Z3VydnRAZ21haWwuY29tIn0sICJ2IjogMH0.lq4IRVfvE
GQklslOlS4uIBLSSJj88YNrloWXvisRgfQ"

result = firebase.get('/users', None, {'print': 'pretty'})
print result
{'1': 'John Doe', '2': 'Jane Doe'}