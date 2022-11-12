from flask import Flask, flash, session, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import pyrebase
import os
import requests
import datetime

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
storage = firebase.storage()
current_path = os.getcwd()

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
            # session['user_object'] = user
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
            return redirect('/login')
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
    if request.method == 'POST': #if form submitted
        user_info = get_user_info()
        # print(user_info)
        try:                 
            item_name = request.form.get('item_name')
            item_price = request.form.get('item_price')
            item_condition = request.form.get('item_condition')
            item_description = request.form.get('item_description')
            seller_fname = user_info.get('firstname')
            seller_lname = user_info.get('lastname')
            seller_email = user_info.get('email')
            image = request.files['item_photo']
            print('image', image)
            posting_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        
            product_id = seller_lname + item_name + posting_time
            
            #storing images to the backend
            storage.child(f'images/posts/{product_id}').put(image)
            image_url = storage.child(f'images/posts/{product_id}').get_url(None)
            posting_data = {
                "firstname": user_info.get('firstname'),
                "lastname": user_info.get('lastname'),
                "email": user_info.get('email'),
                "name": item_name,
                "price": item_price, 
                "condition": item_condition,
                "description": item_description,
                "seller_email": seller_email,
                "seller_lname": seller_lname,
                "posting_time": posting_time,
                "product_id": product_id,
                "image_url": image_url
            }
            db.child("postings").push(posting_data)
            return redirect('/')
        except Exception as e:
            print(e)
            return 'Posting submission failed'
    return render_template('postItem.html') #should go to page that has success message


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/api/posts')
def get_main_feed():
    if ('user' in session):
        all_postings = db.child("postings").get().val()
        postings = list(all_postings.values())
        postings.reverse()
        return postings
    else:
        return None
@app.route('/api/posts/<id>')
def get_image_link(id):
    return storage.child(f"images/posts/{id}").get_url()

# @app.route('/api/file')
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


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