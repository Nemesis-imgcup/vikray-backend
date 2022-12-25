from fastapi import FastAPI, HTTPException, Response
from google.oauth2.credentials import *
from googleapiclient.discovery import build
import google.auth.transport.requests
from google.oauth2.id_token import fetch_id_token_credentials

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Nemesis, I am Vikray    नमस्कार, विक्रय में आपका स्वागत है"}

def get_google_auth_url():
    client_id = "109066387563-ssbpapni2egmjl54p1vgfpb4qjhi0g3c.apps.googleusercontent.com"
    callback_url = "http://127.0.0.1:8000/callback"

    # Using the client ID and callback URL to create the Google login URL
    google_auth_url = "https://accounts.google.com/o/oauth2/v2/auth?client_id=109066387563-ssbpapni2egmjl54p1vgfpb4qjhi0g3c.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:8000/callback&response_type=code&scope=openid%20email%20profile"
    return google_auth_url

@app.get("/login")
def login():
    # Redirecting the user to Google's login page
    google_auth_url = get_google_auth_url()
    # Raising an HTTPException with a status code of 303 and a Location header
    raise HTTPException(status_code=303, headers={"Location": google_auth_url})

def get_user_info(credentials):
    # Using the credentials to retrieve the user's profile information
    user_info_service = build('oauth2', 'v2', credentials=credentials)
    user_info = user_info_service.userinfo().get().execute()
    return user_info

def get_credentials_from_google(code):
    client_id = "109066387563-ssbpapni2egmjl54p1vgfpb4qjhi0g3c.apps.googleusercontent.com"
    client_secret = "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"

    # Use the authorization code to request an ID token from Google
    """IN THIS PART, THE GHAAPLA RESIDES
    
    client_secrets = {"web": {"client_id": client_id, "client_secret": client_secret}}
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    user_agent = "FastAPI"
    scopes = ["openid", "email", "profile"]
    headers = {"User-Agent": user_agent}
    id_token, token_expiry = google.oauth2.id_token.fetch_id_token(
        auth_uri, client_secrets, token_uri, code=code, headers=headers, scopes=scopes
    )

    # Use the ID token to request an access token and refresh token from Google
    credentials = google.oauth2.id_token.fetch_id_token_credentials(
        client_secrets=client_secrets, auth_uri=auth_uri, token_uri=token_uri, id_token=id_token, token_expiry=token_expiry, user_agent=user_agent
    )
    return credentials"""

@app.get("/callback")
def callback(code: str):
    # Using the authorization code to request an access token and refresh token from Google
    credentials = get_credentials_from_google(code)
    # Retrieving the user's profile information
    user_info = get_user_info(credentials)
    return user_info