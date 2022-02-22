from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os

class auth:    
    load_dotenv()
    oauth_token = str(os.getenv("oauth_token"))
    oauth_token_secret = str(os.getenv("oauth_token_secret"))
    consumer_key = str(os.getenv("consumer_key"))
    consumer_secret = str(os.getenv("consumer_secret"))

    def getAuth():
        oAuth = OAuth1Session(
            client_key=auth.consumer_key,
            client_secret=auth.consumer_secret,
            resource_owner_key=auth.oauth_token,
            resource_owner_secret=auth.oauth_token_secret,
        )
        return oAuth


class twitter:
    def post(text):
        oAuth = auth.getAuth()
        response = oAuth.post(
            "https://api.twitter.com/2/tweets",
            json = {"text": text}
        )
        if response.status_code != 201:
            raise Exception("Error: {} {}".format(response.status_code, response.text))
        return {"status_code": response.status_code, "text": response.text}
