import requests
import json
import uwuify

class text:
    class fact:
        funUrl = "https://asli-fun-fact-api.herokuapp.com/"
        uselessUrl = "https://uselessfacts.jsph.pl/random.json?language=en"

        def getFact():
            try:
                r = requests.get(text.fact.funUrl)
                load = json.loads(r.text)
            except requests.exceptions.HTTPError:
                print("Error: Could not connect to FunFact API > Trying Useless Fact API")
                r = requests.get(text.fact.uselessUrl)
                load = json.loads(r.text)
            return load['data']['fact']

        def uwuFact():
            return uwuify.uwu(text.fact.getFact())

    class stoic:
        stoicUrl = "https://stoic-server.herokuapp.com/random"
        backupUrl = "https://api.themotivate365.com/stoic-quote"

        def getStoic():
            try:
                r = requests.get(text.stoic.stoicUrl)
                load = json.loads(r.text)[0]
                return load["body"], load["author"]
            except requests.exceptions.HTTPError:
                print("Error: Could not connect to Stoic API > Trying backup API")
                r = requests.get(text.stoic.backupUrl)
                load = json.loads(r.text)
                return load["data"]["quote"], load["data"]["author"]

        def uwuStoic():
            quote = text.stoic.getStoic()
            return uwuify.uwu(quote[0]) + " - " + quote[1]

    def uwuText():
        return uwuify.uwu(text.getText())


if __name__ == "__main__":
    # # Get Random Fact
    # print(text.fact.getFact())
    # # UwUify Fact
    # print(text.fact.uwuFact())

    # # Get Random Stoic Quote
    # print(text.stoic.getStoic())
    # # UwUify Stoic Quote
    print(text.stoic.uwuStoic())
