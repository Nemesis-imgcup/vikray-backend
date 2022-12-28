import pymongo

# mongoUrl = "mongodb://localhost:27017"
# client = pymongo.MongoClient(mongoUrl)

try:
    client = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    client.server_info()
    # Triggers exception if cannot connect to the database
except:
    print("ACCESS DENIED - Cannot Connect to the Database")

db = client["USERS"]
collection = db["users"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def all_usernames():
    response = collection.find({},{"_id":0,"username":1})
    data = []
    for i in response:
        # i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_one(condition):
    response = collection.find_one({"username":condition})
    response["_id"] = str(response["_id"])
    return response

def update(data):
    data = dict(data)
    response = collection.update_one({"username":data["username"]}, {"$set":{"name":data["name"]}})
    return response.modified_count

def delete(username):
    response = collection.delete_one({"username":username})
    return response.deleted_count