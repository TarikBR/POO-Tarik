import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient["mydatabaseTeste"]

mycol = mydb["dadosTeste"]

mydicty = {
  "_id": "123",
  "data": {
   "name": "teste",
   "price": "12",
   "validate": "ontem",
   "orig": "aki"
  }
 }

#x = mycol.insert_one(mydicty)

#myquery = {"1234":{}}

x = mycol.find()
dataList = [i for i in x]

for data in dataList:
    values = data["data"]
    print(data["data"]["name"])

#print("db: ", mydb)
#print("col: ", mycol)
#print("dbs: ", myclient.list_database_names())
