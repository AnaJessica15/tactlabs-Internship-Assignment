import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://aj_15:**********@cluster0.pdcrn.mongodb.net/aj?retryWrites=true&w=majority")
db = cluster["TactInternship"]
collection = db["TactInternship"]

#CRUD Operations
#Create/Insert
post = {"_id":0,"name":"tim","score":5}
collection.insert_one(post)

post 1 = {"_id":0,"name":"tim","score":5}
post 2 = {"_id":0,"name":"tim","score":5}
collection.insert_many([post1,post2])

#Find
results = collection.find({"name":"tim"})
for result in results:
    print(result)
    
#Delete    
results = collection.delete_one({"_id":0})
results = collection.delete_many({})

#Update
results = collection.update_one({"_id":1},{"$set":{"name":"jill"}
                                           
