class offers():
    temp={
        "name":"",
        "type":"", #takes ethier p or a where p stands for percetage and a for amount
        "value": 3,
        "startDate": 4,
        "endDate": 4
    }



    def __init__(self, mongo):
        self.mongo = mongo
        

    def addoffer(self, offers):
        if(self.mongo.db.offers.find({"name":offers["name"]}).count()):
            return "can't add"
        return str(self.mongo.db.offers.insert(offers))

    def deloffer(self, offers):
        # find offers.name then drop it
        if(self.mongo.db.offers.find({"name":offers["name"]}).count()):
            return str(self.mongo.db.offers.delete_one({"name":offers["name"]}))
        return "offers not found if you updated the name please delete the offers then add again"

    def getoffer(self):
        lst=list()
        for i in self.mongo.db.lists.find({}):
            lst.append(i)
        return i