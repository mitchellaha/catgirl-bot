from PIL import Image, ImageFont, ImageDraw
import textwrap

class image:
    defaultFont = ImageFont.truetype("./src/font/impact.ttf", 55)
    defaultFontPath = "./src/font/impact.ttf"

    def __init__(self, image_path, font=defaultFont):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.draw = ImageDraw.Draw(self.image)
        self.defaultFont = font

    def addText(self, text, textfont=defaultFontPath):
        # Adds Text to the Image
        fontSize = self.findBestTextSize(text)
        font = ImageFont.truetype(textfont, fontSize)
        para = textwrap.wrap(text, width=int(self.width / (fontSize / 2.2)))

        current_h, pad = 40, 20

        # * Find the Total Height of all Lines Of Text Plus the Padding
        textTotalHeight = 0
        for line in range(len(para)):
            lineSize = font.getsize(para[line])
            textTotalHeight = + lineSize[1] + textTotalHeight

        # * Adds Each Line of Text to the Image
        for line in range(len(para)):
            # * Find The Text Size of the Current Line
            lineSize = font.getsize(para[line])
            lineWidth = lineSize[0]
            lineHeight = lineSize[1]

            # ? Determines the best fitting font size for the current line
            while lineWidth > self.width:
                print("Font Size: " + str(fontSize))
                fontSize = fontSize - 2
                font = ImageFont.truetype(textfont, fontSize)
                lineSize = font.getsize(para[line])

            # * Find the Position of the Text with Respect to How Many Lines Of Text
            textPositionX = (self.width / 2) - (lineWidth / 2)
            textPositionY = (self.height - textTotalHeight) - (current_h + pad)
            textPosition = (textPositionX, textPositionY)

            draw = ImageDraw.Draw(self.image)

            draw.text(textPosition, para[line], font=font, fill="white", align="center", stroke_fill="black", stroke_width=5)

            current_h -= lineHeight - pad  # ! To Move the Next Line Down

    def findBestTextSize(self, text):
        # Finds the best font size that keeps the line count under 5
        fontSize = 125
        para = textwrap.wrap(text, width=int(self.width / (fontSize / 2.2)))
        while len(para) > 5:
            fontSize = fontSize - 2
            para = textwrap.wrap(text, width=int(self.width / (fontSize / 2.2)))
        return fontSize

    def save(self, path):
        # Saves The Image at the Defined Path
        self.image.save(path)

if __name__ == "__main__":

    demoText = "Death and pain awe not fwightening, it's the feaw of pain and death we need to feaw. Which is why we pwaise the poet who wwote, 'Death is not feawfuw, but dying wike a cowawd is.'"

    # ! TEST 1
    file = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/TEST.jpg"
    testPic = image(file)
    testPic.addText(demoText)
    savePath = "/Users/mitchellaha/Repositories/catgirl-bot/test.jpg"
    testPic.save(savePath)

    # ! TEST 2
    file2 = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/TEST2.jpg"
    testPic2 = image(file2)
    testPic2.addText(demoText)
    savePath2 = "/Users/mitchellaha/Repositories/catgirl-bot/test2.jpg"
    testPic2.save(savePath2)

    # ! TEST 3
    file3 = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/TEST3.jpg"
    testPic3 = image(file3)
    testPic3.addText(demoText)
    savePath3 = "/Users/mitchellaha/Repositories/catgirl-bot/test3.jpg"
    testPic3.save(savePath3)
