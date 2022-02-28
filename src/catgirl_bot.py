from src.catgirl_api import *
from src.text_api import *
from src.image_edit import *
from src.twitter import *
import logging as log

# check if file exists and if not, create it
def checkFile():
    if not os.path.exists("./catgirl/logs"):
        os.makedirs("./catgirl/logs")
    if not os.path.exists("./catgirl/logs/app.log"):
        with open("./catgirl/logs/app.log", "w") as f:
            f.write("")

checkFile()
log.basicConfig(filename='./catgirl/logs/app.log', filemode='w',
                format='%(asctime)s - %(message)s', level=log.INFO)

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
            log.info("New Stoic Uwu Text Created.")
            newPhoto = catgirl.getCatgirlImage(catgirl.getCatgirlJson(), "catgirl")
            log.info("New Catgirl Image Created." + str(newPhoto["save_path"]))
        else:
            log.debug("Using Existing Catgirl from Dict.")
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
        log.info("Adding Text To Catgirl Image. : " + str(photoPath))
        uwuPic.addText(newText)
        log.info("Saving Catgirl Image. : " + str(savePath))
        uwuPic.save(savePath)

        self.author = photoAuthor
        self.path = savePath

def newStoicCatgirlPost():
    newCatgirl = bot()
    newCatgirl.newStoicCatgirl()
    log.info("Uploading Catgirl to Twitter.")
    upload = twitter.upload(newCatgirl.path)
    mediaID = upload[0]
    author = newCatgirl.author
    if mediaID is not None:
        log.info("Posting Catgirl to Twitter with MediaID :" + str(mediaID))
        twitter.postTextWithImage(f"Author: {author}", mediaID)
        log.info("Post Successful for : " + str(newCatgirl.path))
        # print("Posted: " + str(newCatgirl.path))

if __name__ == "__main__":
    newStoicCatgirlPost()
