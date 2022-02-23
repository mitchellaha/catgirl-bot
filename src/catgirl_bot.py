from catgirl_api import *
from text_api import *
from image_edit import *

class bot:
    def __init__(self):
        self.author = ""
        self.path = ""

    def newStoicCatgirl(self, dict=None):
        if dict is None:
            newText = text.stoic.uwuStoic()
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

if __name__ == "__main__":
    newCatgirl = bot()
    newCatgirl.newStoicCatgirl()
    print("File Location: " + str(newCatgirl.path))
    print("Author: " + str(newCatgirl.author))

    # # TEST 0317.json
    # test0317 = bot()
    # test0317.newStoicCatgirl(dict=open("catgirl/issues/0317.json", "r").read())
    # # print("File Location: " + str(test0317.path))
    # print("Author: " + str(test0317.author))
