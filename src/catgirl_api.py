import requests
import json
import os
from datetime import datetime as dt


class catgirl:
    catgirlUrl = "https://nekos.best/api/v1/nekos"

    def getCatgirl():
        try:
            r = requests.get(catgirl.catgirlUrl)
            load = json.loads(r.text)
        except:
            print("Error: Could not connect to Nekos API")
            r = requests.get(catgirl.catgirlUrl)
            load = json.loads(r.text)
        return load

    def getCatgirlImage(url):
        r = requests.get(url, stream=True)
        time = dt.now().strftime("%Y_%m_%d_%H_%M_%S")
        with open(f"catgirl_{time}.jpg", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return os.path.join(os.getcwd(), f"catgirl-{time}.jpg")

if __name__ == "__main__":
    # Get JSON from Nekos API
    print(catgirl.getCatgirl())
    # Get Image from Nekos API
    print(catgirl.getCatgirlImage(catgirl.getCatgirl()['url']))