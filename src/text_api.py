import requests
import json
import uwuify

def uwuText(text):
    return uwuify.uwu(text)

class fact:
    funUrl = "https://asli-fun-fact-api.herokuapp.com/"
    uselessUrl = "https://uselessfacts.jsph.pl/random.json?language=en"

    def getFact():
        """Gets a random fact from the Asli Fun Fact API.
        
        returns:
            A String with the fact.
        """
        try:
            r = requests.get(fact.funUrl)
            load = json.loads(r.text)
        except requests.exceptions.HTTPError:
            print("Error: Could not connect to FunFact API > Trying Useless Fact API")
            r = requests.get(fact.uselessUrl)
            load = json.loads(r.text)
        return load['data']['fact']

    def uwuFact():
        return uwuify.uwu(fact.getFact())

class stoic:
    stoicUrl = "https://stoic-server.herokuapp.com/random"
    backupUrl = "https://api.themotivate365.com/stoic-quote"

    def getStoic():
        """Gets a random stoic quote from the Stoic API.

        returns:
            A Tuple with the quote and the author.
        """
        try:
            r = requests.get(stoic.stoicUrl)
            load = json.loads(r.text)[0]
            return load["body"], load["author"]
        except requests.exceptions.HTTPError:
            print("Error: Could not connect to Stoic API > Trying backup API")
            r = requests.get(stoic.backupUrl)
            load = json.loads(r.text)
            return load["data"]["quote"], load["data"]["author"]

    def uwuStoic():
        quote = stoic.getStoic()
        return uwuify.uwu(quote[0]) + " - " + quote[1]


if __name__ == "__main__":
    # # Get Random Fact
    # print(fact.getFact())
    # # UwUify Fact
    # print(fact.uwuFact())

    # # Get Random Stoic Quote
    # print(stoic.getStoic())
    # # UwUify Stoic Quote
    print(stoic.uwuStoic())
