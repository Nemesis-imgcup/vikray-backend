from fastapi import FastAPI, HTTPException
import os
import pathlib
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = FastAPI()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "109066387563-ssbpapni2egmjl54p1vgfpb4qjhi0g3c.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            raise HTTPException(status_code=401, detail="Authorization required")
            # return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.get("/")
def root():
    return {"message": "Hello Nemesis, I am Vikray    नमस्कार, विक्रय में आपका स्वागत है"}

