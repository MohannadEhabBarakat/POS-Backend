import bcrypt

class Users():

    def __init__(self, mongo):
        self.mongo = mongo
        

    def addUser(self, Users):
        if(self.mongo.db.Users.find({"name":Users["name"]}).count()):
            return "Already exist"
        Users["password"]=bcrypt.hashpw(Users["password"].encode('utf-8'), bcrypt.gensalt())
        return str(self.mongo.db.Users.insert(Users))

    def delUser(self, Users):
        # find Users.name then drop it
        if(self.mongo.db.Users.find({"name":Users["name"]}).count()):
            return str(self.mongo.db.Users.delete_one({"name":Users["name"]}))
        return "Users not found if you updated the name please delete the Users then add again"

    def getUser(self, name=None):
        if name is not None: return self.mongo.db.Users.find_one({"name":name})
        
        lst=list()
        for i in self.mongo.db.lists.find({}):
            lst.append(i)
        return i

   