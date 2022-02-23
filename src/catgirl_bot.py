from catgirl_api import *
from text_api import *
from image_edit import *

class bot:
    def __init__(self):
        self.author = ""
        self.path = ""

    def newStoicCatgirl(self):
        newText = text.stoic.uwuStoic()
        newPhoto = catgirl.getCatgirlImage(catgirl.getCatgirlJson(), "catgirl")
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

if __name__ == "__main__":
    newCatgirl = bot()
    newCatgirl.newStoicCatgirl()
    print("File Location: " + str(newCatgirl.path))
    print("Author: " + str(newCatgirl.author))
