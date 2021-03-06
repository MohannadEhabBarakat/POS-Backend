from flask import session
from .User import Users
import bcrypt


class Log():
    def __init__(self,app):
        pass

    def login(self, username, password):
        logInUser = User.getUser(username)
        if logInUser:
            if bcrypt.hashpw(password.encode('utf-8'), logInUser['password'].encode('utf-8')) == logInUser['password'].encode('utf-8'):
                session['username'] = username
                session['logggedIn'] = True
                return "You were logged in", logInUser
        return "wrong username or password"

    def logOut(self):
        if session.get("USERNAME") and session['logggedIn'] == True:
            session['logggedIn'] == False
            session.pop("USERNAME", None)
            return "logged out"
        return "Not logged In"

    def isLogedIn(self):
        if session.get("USERNAME") and session['logggedIn'] == True:
            return True
        return False 
    
