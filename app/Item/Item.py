class item():
    temp={
        "name":"hoba",
        "pass":"pass hash",
        "priv":{
            "cash":True,
            "addItem": True,
            "delItem": True,
            "addItem": True,
            "delItem": True,
        },
        "log":[
            {
                "state":"in",
                "time":"1323132132",
            },
            {
                "state":"out",
                "time":"7325345",
            }
        ],
        "amount": 2,
        "owner": ""
    }



    def __init__(self, mongo):
        self.mongo = mongo
        

    def addItem(self, item):
        if(self.mongo.db.items.find({"name": item["name"]}).count()):
            return "can't add"
        return str(self.mongo.db.items.insert(item))
        

    def modItem(self, item):
        # find item.name then update all of it's values 
        if(self.mongo.db.items.find({"name":item["name"]}).count()):
            self.mongo.db.items.delete_one({"name":item["name"]})
            return str(self.mongo.db.items.insert(item))
        return "item not found if you updated the name please delete the item then add again"



    def delItem(self, item):
        # find item.name then drop it
        if(self.mongo.db.items.find({"name":item["name"]}).count()):
            return str(self.mongo.db.items.delete_one({"name":item["name"]}))
        return "item not found if you updated the name please delete the item then add again"

    def getItem(self):
        lst=list()
        for i in self.item.db.lists.find({}):
            lst.append(i)
        return i

    def decreaseAmount(self, item):
        if(self.mongo.db.items.find({"name":item["name"]}).count()):
            self.mongo.db.items.update_one({"name":item["name"]} , {"$dec": {"ammount":1}})

    def increaseAmount(self, item):
        if(self.mongo.db.items.find({"name":item["name"]}).count()):
            self.mongo.db.items.update_one({"name":item["name"]} , {"$inc": {"ammount":1}})

