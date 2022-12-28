from pydantic import BaseModel

class Users(BaseModel):
    username: str
    name: str
    picture: str

    def to_json(self):
        return {
            "username": self.username,
            "name": self.name,
            "picture": self.picture
        }