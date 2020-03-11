from .User import Users as US
from .Log import Log 

def user(mongo):
    return US(mongo)

def log(app):
    return Log(app)



