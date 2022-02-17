import requests
import json

class fact:
    funUrl = "https://asli-fun-fact-api.herokuapp.com/"
    uselessUrl = "https://uselessfacts.jsph.pl/random.json?language=en"

    def getFact():
        r = requests.get(fact.funUrl)
        load = json.loads(r.text)
        return load['data']['fact']

print(fact.getFact())

