from flask import Flask, request
from flask_pymongo import PyMongo
from .User import user
# from .List.List import lists
# from .Item.Item import item
import os

MONGO_URI = os.environ.get("MONGO_URI")

app = Flask(__name__)

print("DB URI: ",MONGO_URI)
app.config["MONGO_URI"]=MONGO_URI

mongo = PyMongo()
mongo.init_app(app)
tempUser=user(mongo)
# tempCat=lists(mongo)
# tempItem=item(mongo)
# tempOffer=offer(mongo)
# tempCash= cash(mongo)
# tempReturn=returns(mongo)



@app.route('/')
def home():
    return "hi 3la elnas el hay"

@app.route('/addUser', methods=['POST'])
def addUser():
    use=request.get_json()
    print(use)
    return tempUser.addUser(use)


# @app.route('/modUser')
# def modUser():
#     use=request.get_json()
#     return tempUser.modUser(use)

# @app.route('/delUser')
# def delUser():
#     use=request.get_json()
#     return tempUser.delUser(use)

# @app.route('/getUsers')
# def getAllUsers():
#     return tempUser.getUser()

# @app.route('/addCat')
# def addCat():
#     cat=request.get_json()
#     return tempCat.addCat("tst")

# @app.route('/delCat')
# def delCat():
#     cat=request.get_json()
#     return tempCat.delCat("tst")

# @app.route('/getCat')
# def getAllCats():
#     return str(tempCat.getCat())

# @app.route('/addItem')
# def addItem():
#     item=request.get_json()
#     tempItem.addItem(item)

# @app.route('/delItem')
# def delItem():
#     item=request.get_json()
#     tempItem.delItem(item)

# @app.route('/modItem')
# def modItem():
#     item=request.get_json()
#     tempItem.modItem(item)

# @app.route('/getAllItems')
# def geAllItems():
#     return tempItem.getItem()

# @app.route('/addOffer')
# def addOffer():
#     offer=request.get_json()
#     return tempOffer.addOffer("tst")

# @app.route('/delOffer')
# def delOffer():
#     offer=request.get_json()
#     tempOffer.delOffer(offer)

# @app.route('/getAllOffers')
# def geAllOffers():
#     return tempOffer.getOffer()

# @app.route('/getPriv')
# def geAllprivs():
#     return tempCat.getAllPriv()

# @app.route('/addToScanner')
# def addToScanner():
#     pass

# @app.route('/getAndDelScanner')
# def getScanner():
#     pass

# @app.route('/cash')
# def CASH():
#     order=request.get_json()
#     return tempCash.CASH(order)

# @app.route('/retuenItem')
# def retuenItem():
#     item=request.get_json()
#     tempItem.decreaseAmount(item)
#     tempReturn.addReturn (item)

    


if __name__ =="__main__":
    app.run()
