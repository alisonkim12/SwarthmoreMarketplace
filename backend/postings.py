import pyrebase
from app import *

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

""" posting information: first name, last name, email, Item name, Price, Item condition, Item description, photo (id) jpeg/png file"""

""" way to get user info (firstname, lastname, email) based on who is logged in"""
user_info = get_users_info()
print(user_info) 


app.route('/postItem', methods = ['GET', 'POST'])
def postItem():
    item_name = request.form.get('item_name')
    item_price = request.form.get('item_price')
    item_condition = request.form.get('item_condition')
    item_description = request.form.get('item_description')
    #idk how photos uploaded from the frontend translates into the backend and how to store the data
    if request.method == 'POST': #if form submitted
        try: #register
            #user = auth.create_user_with_email_and_password(email, password)
            posting_data = {
                "item_name": item_name,
                "item_price": item_price,
                "item_condition": item_condition
                "item_description": item_description
                #item_photo: item_photo? 
            }
            db.child("postings").push(posting_data, user['idToken'])
        except Exception as e:
            print(e)
            return 'Posting submission failed'
    return render_template('postItem.html')




