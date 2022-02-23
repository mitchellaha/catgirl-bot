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

        current_h, pad = 40, 10

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
            print("LineWidth:" + str(lineWidth) + "  Image Width: " + str(self.width))
            while lineWidth > self.width:
                print("")
                print(f"ADJUSTING FONT SIZE FOR LINE: {para[line]}")
                print(f"LineWidth: {lineWidth}")
                print(f"Image Width: {self.width}")
                fontSize = fontSize - 1
                print(f"Adjusted Font Size: {fontSize}")
                font = ImageFont.truetype(textfont, fontSize)
                lineSize = font.getsize(para[line])
                lineWidth = lineSize[0]
                lineHeight = lineSize[1]

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

        wordCount = len(text.split())
        print(f"Word Count: {wordCount}")
        if wordCount >= 40:  # ? Probably a More Pythonic Way to Do This / Will Return Later
            maxLines = 6
        if wordCount < 40:
            maxLines = 5
        if wordCount <= 30:
            maxLines = 4
        if wordCount <= 20:
            maxLines = 3
        while len(para) > maxLines:
            fontSize = fontSize - 1
            para = textwrap.wrap(text, width=int(self.width / (fontSize / 2.2)))
        return fontSize

    def save(self, path):
        # Saves The Image at the Defined Path
        self.image.save(path)

if __name__ == "__main__":
    demoText = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec,
    pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, """
    # # ! TEST 1
    file = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/0517.jpg"
    testPic = image(file)
    testPic.addText(demoText)
    savePath = "/Users/mitchellaha/Repositories/catgirl-bot/0517_uwu.jpg"
    testPic.save(savePath)

    # # ! TEST 2
    # file = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/TEST4.jpg"
    # testPic = image(file)
    # testPic.addText(demoText)
    # savePath = "/Users/mitchellaha/Repositories/catgirl-bot/TEST4_UWU.jpg"
    # testPic.save(savePath)

    # demoText3 = "Practice, Yourself, Because, Practice Yourself Lorem Ipsum Standard Texts Pwactice youwsewf, fow heaven's sake, in wittwe things; and thence pwoceed to gweata - Epictetus"
    # # ! TEST 3
    # file2 = "/Users/mitchellaha/Repositories/catgirl-bot/catgirl/0517.jpg"
    # testPic2 = image(file2)
    # testPic2.addText(demoText3)
    # savePath2 = "/Users/mitchellaha/Repositories/catgirl-bot/0517_UWU2.jpg"
    # testPic2.save(savePath2)
