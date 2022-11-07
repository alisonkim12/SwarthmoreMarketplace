from flask import Flask, session, render_template, request, redirect, send_from_directory
import pyrebase
import requests

app = Flask(__name__)

config = {
  'apiKey': "AIzaSyBPwmDxLcv11-nhDhmwq1Jqt6Q2sQ9XccY",
  'authDomain': "swarthmoremarketplace.firebaseapp.com",
  'projectId': "swarthmoremarketplace",
  'storageBucket': "swarthmoremarketplace.appspot.com",
  'messagingSenderId': "410170758850",
  'appId': "1:410170758850:web:efc1a435d0d065d26d4d5b",
  'measurementId': "G-1YP7TGS9CT",
  'databaseURL': "https://swarthmoremarketplace-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.secret_key = 'secret'

@app.before_request
def before_request():
    if 'user' in session:
        return None
    elif request.path == '/login':
        return
    elif request.path == '/register':
        return
    elif request.path == '/public/stylesheets/styles.css':
        return
    else:
        return redirect('/login')

@app.route("/")
def get_main_page():
    return render_template('main.html')

@app.route('/login', methods = ['POST', 'GET'])
def login(): 
    if ('user' in session):
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST': #if form submitted
        email = request.form.get('email')
        password = request.form.get('password')
        try: #login
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email #assign user variable to session
            print('log in', session)
            return redirect('/')
            #return f'Hi, {email}'
        except Exception as e: #login does not go through  
            #print(e)
            return 'Failed to Login'
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    if request.method == 'POST': #if form submitted
        try: #register
            user = auth.create_user_with_email_and_password(email, password)
            user_data = {
                "firstname": first_name,
                "lastname": last_name,
                "email": email
            }
            db.child("users").push(user_data, user['idToken'])
            print(user)
            return f'Successfully registered account with {email}'
        except Exception as e:
            print(e)
            return 'Register failed'
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/postItem', methods = ['GET', 'POST'])
def postItem():
    item_name = request.form.get('item_name')
    item_price = request.form.get('item_price')
    item_condition = request.form.get('item_condition')
    item_description = request.form.get('item_description')
    #imagefile = flask.request.files.get('item_photo', '')

    #idk how photos uploaded from the frontend translates into the backend and how to store the data
    if request.method == 'POST': #if form submitted
        try: #register
            #user = auth.create_user_with_email_and_password(email, password)
            posting_data = {
                "item_name": item_name,
                "item_price": item_price, 
                "item_condition": item_condition,
                "item_description": item_description
                #item_photo: item_photo? 
            }
            db.child("postings").push(posting_data, user['idToken'])
        except Exception as e:
            print(e)
            return 'Posting submission failed'
    return render_template('postItem.html')

@app.route('/api/user')
def get_user_info():
    if ('user' in session):
        user = session['user']
        print(user)
        user_info = auth.get_account_info(user['idToken'])
        return user_info
        #once we have info in database, use user info to find entry in database and return that row
    else:
        return None

@app.route('/public/stylesheets/styles.css')
def get_styling():
    return send_from_directory('static', 'styles.css')

#extra methods

#user = auth.create_user_with_email_and_password(email, password)
#print(user)

#user = auth.sign_in_with_email_and_password(email, password)

#info = aut.get_account_info(user['idToken'])
#print(info)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)

if __name__ == '__main__':
    app.run() # run locally