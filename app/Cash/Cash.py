class cash():
    temp={
        "selledBy": "",
        "selledTo": "",
        "soldItems": ""

    }



    def __init__(self, mongo):
        self.mongo = mongo
        

    def CASH (self, order):
        return str(self.mongo.db.orders.insert(order))

    