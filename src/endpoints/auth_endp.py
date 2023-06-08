from fastapi import  APIRouter
from src.models.auth_model import Login
import requests

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

hostname = "https://api.staging.tides.coloredcow.com"

test_db = {
    "user1":{
        "phone": "917834811114",
        "password": "secret1234",
        "access_token": "",
        "renewal_token": "",
        "token_expiry_time": ""
    }
}


#make a post request to glific API
def post_glific(url, headers, payload):
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making POST request: {e}")
        return None


#When Users login, they will call glific API to get access token
@router.post("/login")
async def login(credentials: Login):

    if len(credentials.phone)<0 or len(credentials.password)<0:
        return {"message": "Phone or Password is missing"}
    
    """
        YOUR AUTHENTICATION LOGIC GOES HERE
    """

    path = "/api/v1/session"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    #FOR TESTING USE
    # PHONE: 917834811114
    # PASSWORD: secret1234  
    payload = {
       "user": {
            "phone": credentials.phone,
            "password": credentials.password
        }
    }

    token_data = post_glific(hostname+path, headers, payload)

    if token_data is None:
        return {"error": "failed to fetch access token"}
    
    print(token_data)

    #after receiving the access token, we have to store it somewhere
    #for now we will just Store in python dictionary
    test_db["user1"]["access_token"] = token_data["data"]["access_token"]
    test_db["user1"]["renewal_token"] = token_data["data"]["renewal_token"]
    test_db["user1"]["token_expiry_time"] = token_data["data"]["token_expiry_time"]

    return {"success" : "login successful"}