## import the libraries
import tweepy, codecs
from aylienapiclient import textapi



## fill in your Twitter credentials 
consumer_key = 'n4RXGtbkQs3WSfgcJb4YfJ9yc'
consumer_secret = 'edUBqt7WcGessBTY6K7C9ftS1QOtriT9ZjOYTVEeyH8cHPsJD0'
access_token = '3449013974-ZWxCu7yzolQrS45Aojtswebe7lHFN81L15rToGo'
access_token_secret = 'OaLVyPlirIMKv5b14QvW0y8MIES96hD6wb38LoUia7RaJ'
## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## fill in your search query and store your results in a variable
results = api.search(q = "raspberry", lang = "en", result_type = "recent", count = 10000)

## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("yasser.txt", "w", "utf-8")
for result in results:
	file.write("\n"  +  "\n" + result.text + "\n")
	file.write("\n"+  "+++++++++++++++++++++++++++++++++++\n")
file.close()