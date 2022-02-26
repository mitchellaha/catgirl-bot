import requests
import json
import os
from datetime import datetime as dt


class catgirl:
    catgirlUrl = "https://nekos.best/api/v1/nekos"

    def getCatgirlJson():
        """
        Gets a catgirl from the Nekos API and returns a Dictionary Object

        returns:
            A Dictionary Object with the following keys:
                source_url: The URL of the image
                artist_href: The URL of the artist
                artist_name: The name of the artist
                url: The Direct URL of the image
        """
        try:
            r = requests.get(catgirl.catgirlUrl)
            load = json.loads(r.text)
        except requests.exceptions.HTTPError:
            print("Error: Could not connect to Nekos API")
            r = requests.get(catgirl.catgirlUrl)  # ! This Is Useless, Needs To Be Changed/Removed
            load = json.loads(r.text)  # ! This Is Useless, Needs To Be Changed/Removed
        return load

    def getCatgirlImage(apiJSON, savePath):
        """
        Takes a JSON Object from the Nekos API and saves the image to the defined path with the information as .json file.
        
        args:
            apiJSON: A Dictionary Object from the Nekos API.
            savePath: The path to save the image and the .json file.

        returns:
            A Dictionary Object with the following keys:
                source_url: The URL of the image
                artist_href: The URL of the artist
                artist_name: The name of the artist
                url: The Direct URL of the image
                save_path: The path to the saved image
                save_time: The time the image was saved
        """
        url = apiJSON["url"]
        r = requests.get(url, stream=True)

        urlBasename = os.path.basename(url)
        path = os.path.join(savePath, urlBasename)

        with open(path, 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()

        apiJSON["save_time"] = dt.now().strftime("%Y-%m-%d_%H:%M:%S")
        apiJSON["save_path"] = path
        os.path.splitext(urlBasename)[0]

        with open(os.path.join(savePath, os.path.splitext(urlBasename)[0] + ".json"), 'w') as f:
            json.dump(apiJSON, f, indent=4, ensure_ascii=False)

        return apiJSON


if __name__ == "__main__":
    saveFolder = os.path.join(os.getcwd(), "catgirl")
    # Get JSON from Nekos API
    print(catgirl.getCatgirlJson())
    # Get Image from Nekos API
    print(catgirl.getCatgirlImage(catgirl.getCatgirlJson(), saveFolder))
