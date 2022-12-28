from app import app

from database import db
from model import models

@app.route("/all")
def get_all():
    data = db.all()
    return data

@app.route("/allusernames")
def get_allusernames():
    data = db.all_usernames()
    return data

@app.route("/create", methods=["POST"])
def create(data: models.Users):
    data = models.Users(
        username=data.username,
        name=data.name,
        picture=data.picture,
        )
    id = db.create(data)
    return {"inserted": True, "inserted_id": id}

@app.route("/get")
def get_one(username: str):
    data = db.get_one(username)
    return {"data": data}

@app.route("/delete", methods=["DELETE"])
def delete(username: str):
    data = db.delete(username)
    return {"deleted": True, "deleted_count": data}

@app.route("/update", methods=["PUT"])
def update(data: models.Users):
    user = models.Users(username=data.username, name=data.name)
    data = db.update(user)
    return {"updated": True, "updated_count": data}