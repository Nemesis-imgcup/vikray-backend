from fastapi import FastAPI
import db
import models

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Nemesis, I am Vikray    नमस्कार, विक्रय में आपका स्वागत है"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data":data}

@app.get("/allusernames")
def get_allusernames():
    data = db.all_usernames()
    return {"data":data}

@app.post("/create")
def create(data: models.Users):
    data = models.Users(username=data.username, password=data.password)
    id = db.create(data)
    return {"inserted": True, "inserted_id": id}

@app.get("/get/{username}")
def get_one(username:str):
    data = db.get_one(username)
    return {"data":data}


@app.delete("/delete")
def delete(username:str):
    data = db.delete(username)
    return {"deleted": True, "deleted_count": data}

@app.put("/update")
def update(data:models.Users):
    data = db.update(data)
    return {"updated": True, "updated_count": data}