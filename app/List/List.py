class lists():
    cat={
        "name" : "cat",
        "value" : ["حلو","حادق"]
    }
    priv={
        "name" : "cat",
        "value" : ["cash",""]
    }


    def __init__(self, mongo):
        self.mongo = mongo
        if(self.mongo.db.lists.find({"name":"cat"}).count()==0):
            self.mongo.db.lists.insert(self.cat)
        
        if(self.mongo.db.lists.find({"name":"priv"}).count()==0):
            self.mongo.db.lists.insert(self.priv)

    def addCat(self, cat):
        x=self.mongo.db.lists.find({"name":"cat"})
        print(x.count())
        if(x.count()):
            lst=x[0]["value"]
            if(cat not in lst):
                lst.append(cat)
                self.mongo.db.lists.update_one({"name":"cat"},{"$set":{"value":lst}})
                return "done"
            return "already exists"

        return "error"

    def delCat(self, cat):
        x=self.mongo.db.lists.find({"name":"cat"})
        print(x.count())
        if(x.count()):
            lst=x[0]["value"]
            if(cat in lst):
                lst.remove(cat)
                self.mongo.db.lists.update_one({"name":"cat"},{"$set":{"value":lst}})
                return "done"
            return "don't exists"

        return "error"

    def getCat(self):
        lst=list()
        for i in self.mongo.db.lists.find({"name":"cat"})[0]["value"]:
            lst.append(i)
        return i
    
    def getAllPriv(self):
        lst=list()
        for i in self.mongo.db.lists.find({"name":"priv"})[0]["value"]:
            lst.append(i)
        return i

    