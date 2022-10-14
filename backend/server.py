from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_main_page():
    return render_template('main.html')

"""@app.route('/logout')
def bye():
    return '<h1>Goodbye!</h1>'"""

if __name__ == '__main__':
    app.run() # run locally