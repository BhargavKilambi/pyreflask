"""
Basic Flask app integrated with Firebase using Pyrebase
"""
#imports
from flask import Flask,render_template,request,redirect
import pyrebase
import sys
#saving firebase config in a class
from config1 import Config1
#init flask
app = Flask(__name__)
user = None
user_1 = False

#config firebase
c1 = Config1()
firebase  = pyrebase.initialize_app(c1.giveConfig())
auth = firebase.auth()
database = firebase.database()

##SIMPLE ROUTES##

#error route
@app.route('/error')
def err():
    return 'Error 404'
#home route
@app.route('/')
def home():
    global user_1
    if user_1:
        user = auth.current_user
        return render_template('home.html',u=user)
    else:
        return render_template('login.html')

#login to firebase
@app.route('/signin',methods=['POST','GET'])
def login():
    print(request.method)
    global user_1
    if request.method == 'POST':
        formdata = request.form
        try:
            user = auth.sign_in_with_email_and_password(formdata['email'],formdata['password'])
        except:
            if len(formdata['password'])<8:
                error = "* Password must be atleast 8 characters"
            else:
                error = "* Invalid email/password"
            return render_template('login.html',error = error)
        finally:
            user_1 = True
            user = user
            return redirect('/')
        if user:
            user_1 = True
            user = user
            return redirect('/')
        else:
            error = "* Invalid email/password"
            return render_template('login.html',error = error)
    else:
        return redirect('/error')

#signout
@app.route('/signout')
def logout():
    global user_1
    if auth.current_user:
        user_1 = False
        user = None
        return redirect('/')
    else:
        user_1 = False
        return redirect('/')

@app.route('/pushdata')
def pushit():
    user = auth.current_user
    db = firebase.database()
    data = {
        "name":"Bhargav Ram"
    }
    db.child("users").push(data,user['idToken'])
    return redirect('/')

#app main route
if __name__ == "__main__":
    app.run(debug = True)