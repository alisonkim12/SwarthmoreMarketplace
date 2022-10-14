from flask import Flask

app = Flask(__name__)

@app.route("/api/users")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/logout')
def bye():
    return '<h1>Goodbye!</h1>'

if __name__ == '__main__':
    app.run() # run locally