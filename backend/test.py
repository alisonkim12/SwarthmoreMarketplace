import pyrebase

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

def create_user(auth, db, email, firstname, lastname, password):
    user = auth.create_user_with_email_and_password(email, password)
    user_data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email
    }
    db.child("users").push(user_data, user['idToken'])
    return user

def sign_in_user(auth, email, password):
    return auth.sign_in_with_email_and_password(email, password)

def get_all_users(db):
    return db.child("users").get().val().values()

def list_item_for_sale(db, name, description, price):
    item_data = {
        "name": name,
        "description": description,
        "price": price
    }
    return db.child("items").push(item_data)

# Test 1
new_user = create_user(auth, db, "test123456@example.com", "ABC", "XYZ", "123456")
print(str(new_user))
existing_user = sign_in_user(auth, "mwehar1@swarthmore.edu", "123456")
print(str(existing_user))

# Test 2
print(get_all_users(db))

# Test 3
print(str(list_item_for_sale(db, "pillow", "large fluffy bed pillow", "$10.00")))
