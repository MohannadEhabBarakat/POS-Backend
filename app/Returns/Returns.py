
class return():
    temp={
      "item":"", # = {"name":"", "owner":""}
      "time":3,
      "returnedBy": "",
      "cashID" : "" , 
      "reason" : ""

    }



    def __init__(self, mongo):
        self.mongo = mongo
    

    def addReturn(self,returns):
        self.mongo.db.returns.insert(returns))
    