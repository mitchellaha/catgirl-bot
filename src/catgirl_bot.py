from src.catgirl_api import *
from src.text_api import *
from src.image_edit import *
from src.twitter import *

class bot:
    def __init__(self):
        self.author = ""
        self.path = ""

    def newStoicCatgirl(self, dict=None):
        """
        Gets a new catgirl from the Nekos API adds Stoic Uwu Text to it and save it.

        args:
            dict: A dictionary object thats been created previously.

        sets the object's uwu catgirl path and author attributes.
        """
        if dict is None:
            newText = stoic.uwuStoic()
            newPhoto = catgirl.getCatgirlImage(catgirl.getCatgirlJson(), "catgirl")
        else:
            test = json.loads(dict)
            newText = test["text"]
            newPhoto = test
        
        newPhoto["text"] = newText

        photoPath = newPhoto["save_path"]
        photoAuthor = newPhoto["artist_name"]

        basename = os.path.basename(photoPath)
        savePath = os.path.join("catgirl", os.path.splitext(basename)[0] + "_uwu" + os.path.splitext(basename)[1])
        newPhoto["uwu_path"] = savePath

        # save newphoto dictionary to the json file
        with open(os.path.join("catgirl", os.path.splitext(os.path.basename(newPhoto["url"]))[0] + ".json"), 'w') as f:
            json.dump(newPhoto, f, indent=4, ensure_ascii=False)

        uwuPic = image(photoPath)
        uwuPic.addText(newText)
        uwuPic.save(savePath)

        self.author = photoAuthor
        self.path = savePath

def newStoicCatgirlPost():
    newCatgirl = bot()
    newCatgirl.newStoicCatgirl()
    upload = twitter.upload(newCatgirl.path)
    mediaID = upload[0]
    author = newCatgirl.author
    if mediaID is not None:
        print(twitter.postTextWithImage(f"Author: {author}", mediaID))
        print("Posted: " + str(newCatgirl.path))

if __name__ == "__main__":
    newStoicCatgirlPost()
