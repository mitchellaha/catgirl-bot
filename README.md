# catgirl-bot
A Python Bot That UwUifys a random ~~fact~~ **stoic quote**, puts it on a photo of a catgirl, then posts to twitter.

This is a Twitter Bot Made For **[@TheCatGirlBot](https://twitter.com/TheCatGirlBot)**

## Ideas

- Maybe Setup Flask for a web interface? 
- Maybe Something in addition to stoic quotes? Astrology or something?
- [Instagram Posting](https://www.geeksforgeeks.org/post-a-picture-automatically-on-instagram-using-python/) with CatGirl-Bot?
- ["StyleGan-2 Generating Catgirls?"](https://github.com/EdZ543/This-Catgirl-Does-Not-Exist") (EdZ543)
- [FaceSwapping?](https://github.com/shaoanlu/faceswap-GAN)


## CatGirl API Info

- JPEG Endpoint: https://nekos.best/api/v1/nekos
- GIF Endpoint: https://nekos.best/api/v1/{type}

Gif Types:
```
baka, bite, blush, bored, cry,
cuddle, dance, facepalm, feed,
happy, highfive, hug, kiss, laugh,
pat, poke, pout, shrug, slap,
sleep, smile, smug, stare, think,
thumbsup, tickle, wave, wink
```


## Python Setup

*Tested Python Versions: 3.9.9 and 3.9.10*

1. ```$ python -m venv env```
2. ```$ source venv/bin/activate```
3. ```$ pip install -r requirements.txt```

## Environment Variables Needed

*catgirl-Bot is setup to load them from just a .env file*

~~~
oauth_token = [OAUTH_TOKEN]
oauth_token_secret = [OAUTH_TOKEN_SECRET]
consumer_key = [CONSUMER_KEY]
consumer_secret = [CONSUMER_SECRET]
~~~

## Docker Setup

- To Build: ```$ docker build -t catgirl-bot .```
- To Run With Compose: ```$ docker-compose up -d```

## Resources

- [UwUify Text Generator](https://github.com/StarrFox/uwuify)
- [Random Fun Fact](https://asli-fun-fact-api.herokuapp.com/)
- [Random Useless Fact](https://uselessfacts.jsph.pl/)
- [Better Stoic Quotes](https://stoic-server.herokuapp.com/random)
- [Stoic Quotes](https://github.com/tlcheah2/stoic-quote-lambda-public-api)
- [Better CatGirl API](https://docs.nekos.best/)


### Other Resources

- [All Free APIs](https://github.com/public-apis/public-apis)
- [Fuck Off API](https://www.foaas.com/)
- [SHOUTCLOUD](http://shoutcloud.io/)
- [Catgirl API](https://www.nekos.fun/apidoc.html)
- [Waifu API](https://waifu.im/docs/)
- [Facts From Number](http://numbersapi.com/#42)
