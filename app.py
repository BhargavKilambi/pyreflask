from flask import Flask,render_template
import pyrebase

app = Flask(__name__)
user_1 = False
config = {
    "apiKey": "AIzaSyDNfqGKMpgclIHcpl4-kbTwRAtTHBkH1pU",
    "authDomain": "pytrial-cd85e.firebaseapp.com",
    "databaseURL": "https://pytrial-cd85e.firebaseio.com",
    "projectId": "pytrial-cd85e",
    "storageBucket": "pytrial-cd85e.appspot.com",
    "messagingSenderId": "669169177880"
}
firebase  = pyrebase.initialize_app(config)
@app.route('/')
def home():
    if user_1:
        return render_template('home.html')
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug = True)