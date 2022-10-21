from flask import Flask, session, render_template, request, redirect
import pyrebase
import create_user_with_email_and_password

app = Flask(__name__)

config = {
  'apiKey': "AIzaSyBPwmDxLcv11-nhDhmwq1Jqt6Q2sQ9XccY",
  'authDomain': "swarthmoremarketplace.firebaseapp.com",
  'projectId': "swarthmoremarketplace",
  'storageBucket': "swarthmoremarketplace.appspot.com",
  'messagingSenderId': "410170758850",
  'appId': "1:410170758850:web:efc1a435d0d065d26d4d5b",
  'measurementId': "G-1YP7TGS9CT",
  'databaseURL': ''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

@app.route('/', methods = ['POST', 'GET'])
def index(): 
    if ('user' in session):
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST': #if form submitted
        email = request.form.get('email')
        password = request.form.get('password')
        try: #login
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email #assign user variable to email
            print('made it here')
            return 'Hi, {}'.format(session['user'])
        except: #login does not go through
            return 'Failed to Login'
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registerflask.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

if __name__ == '__main__':
    app.run() # run locally