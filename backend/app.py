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
        return redirect('/')
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

@app.route('/api/user')
def get_user_info():
    if ('user' in session):
        user_email = session['user']
        try:
            user_object = db.child("users").order_by_child("email").equal_to(user_email).get()
            user_info = None
            for user in user_object.each(): #figure out if there's an easier way to do this
                user_info = user.val()
            return user_info

        except Exception as e:
            print(e)
            return 'Failed to get user info'
    else:
        return None



@app.route('/postItem', methods = ['GET', 'POST'])
def postItem():
    item_name = request.form.get('item_name')
    item_price = request.form.get('item_price')
    item_condition = request.form.get('item_condition')
    item_description = request.form.get('item_description')

    #storing images to the backend
    """
    upload_path = current_path + '/images'
    def upload_file():
        if request.method == 'POST':
            photo_file = request.files['item_photo"']
            if photo_file.filename != '':
                file_extension = photo_file.filename.split(".")[-1]
                # must create or get a product_id
                output_filepath = upload_path + '/templates/' + product_id + '.' + file_extension
                photo_file.save(output_filepath) #saves file to uploaded file
                return render_template("next.html")
            else:
                return 'failure'
        else:
            return render_template("current.html")

    """

    #idk how photos uploaded from the frontend translates into the backend and how to store the data
    if request.method == 'POST': #if form submitted
        try: #register
            #user = auth.create_user_with_email_and_password(email, password)
            posting_data = {
                "firstname": user_info.get('firstname'),
                "lastname": user_info.get('lastname'),
                "email": user_info.get('email'),
                "item_name": item_name,
                "item_price": item_price, 
                "item_condition": item_condition,
                "item_description": item_description
                #item_photo: item_photo? if it is inside the templates file we can access it that way instead of storing it in the firebase console 
            }
            db.child("postings").push(posting_data, user['idToken'])
        except Exception as e:
            print(e)
            return 'Posting submission failed'
    return render_template('postItem.html')



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