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
    def textPost(text):
        """Posts Text to Twitter.

        args:
            text: The Text to Post.
        returns:
            :The full JSON response from twitter. [0]
            :The status code of the response. [1]
        """
        oAuth = auth.getAuth()
        response = oAuth.post(
            "https://api.twitter.com/2/tweets",
            json={"text": text}
        )
        if response.status_code != 201:
            raise Exception("Error: {} {}".format(response.status_code, response.text))
        data = response.json()
        return data, response.status_code

    def postImage(media_id):
        """Post an image to twitter.
        
        args:
            media_id: The media_id of the image to post.
        returns:
            The full JSON response from twitter. [0]
        """
        oAuth = auth.getAuth()
        response = oAuth.post(
            "https://api.twitter.com/2/tweets",
            json={"media": {"media_ids": [str(media_id)]}}
        )
        if response.status_code != 201:
            raise Exception("Error: {} {}".format(response.status_code, response.text))
        data = response.json()
        return data, response.status_code

    def postTextWithImage(text, mediaID):
        """Posts Text with an Image to Twitter.

        args:
            text: The Text to Post.
            mediaID: The media_id of the image to post.
        returns:
            :The full JSON response from twitter. [0]
            :The status code of the response. [1]
        """
        oAuth = auth.getAuth()
        response = oAuth.post(
            "https://api.twitter.com/2/tweets",
            json={"text": text, "media": {"media_ids": [str(mediaID)]}}
        )
        if response.status_code != 201:
            raise Exception("Error: {} {}".format(response.status_code, response.text))
        data = response.json()
        return data, response.status_code

    def binary(file):  # ! PROBABLY NOT NEEDED
        with open(file, "rb") as image:
            f = image.read()
            b = bytearray(f)
            return b[0]

    def upload(file):
        """Uploads a Image To Twitter.

        args:
            file: The Location of the file to upload.
        returns:
            The media_id of the uploaded image. [0]
            full JSON response from twitter. [1]
        """
        oAuth = auth.getAuth()
        response = oAuth.post(
            "https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image",
            files={"media": open(file, "rb")}
        )
        if response.status_code != 200:
            raise Exception("Error: {} {}".format(response.status_code, response.text))
        data = response.json()
        return data["media_id"], data

if __name__ == "__main__":
    upload = twitter.upload("./catgirl/issues/0281.jpg")
    mediaID = upload[0]
    if mediaID is not None:
        print(twitter.postTextWithImage("test", mediaID))
