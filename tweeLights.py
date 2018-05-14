## import the libraries
import tweepy, codecs, os, sys
from aylienapiclient import textapi


def setupTwitterAuth(file):
	global authentication_data
	if not os.path.isfile("config.txt"):
		print("File path {} does not exist. Exiting...".format("config.txt"))
		sys.exit()
	try:
		file=codecs.open("config.txt", "r", "utf-8")
		authentication_data= file.readlines();

		if authentication_data[0].__contains__("consumer_key"):
			authentication_data[0]= authentication_data[0].lstrip("consumer_key:")
			authentication_data[0]=authentication_data[0].strip()
			print(authentication_data[0])
		else:
			raise (ValueError)

		if authentication_data[1].__contains__("consumer_secret:"):
			authentication_data[1]=authentication_data[1].lstrip("consumer_secret:")
			authentication_data[1]=authentication_data[1].strip()
			print(authentication_data[1])
		else:
			raise (ValueError)

		if authentication_data[2].__contains__("access_token:"):
			authentication_data[2]=authentication_data[2].lstrip("access_token:")
			authentication_data[2]=authentication_data[2].strip()
			print(authentication_data[2])
		else:
			raise (ValueError)

		if authentication_data[3].__contains__("access_token_secret:"):
			authentication_data[3]=authentication_data[3].lstrip("access_token_secret:")
			authentication_data[3]=authentication_data[3].strip()
			print(authentication_data[3])
		else:
			raise(ValueError)

	except ValueError:
		print("The data is not formatted as required whithin your config.txt file. Please reformat it by referring to the user manual!")


setupTwitterAuth("config.txt")

## fill in your Twitter credentials
consumer_key = authentication_data[0]
consumer_secret = authentication_data[1]
access_token = authentication_data[2]
access_token_secret = authentication_data[3]


## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## fill in your search query and store your results in a variable
results = api.search(q = "@tweeLightsSWE", lang = "en", result_type = "recent", count = 10000)


## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("yasser.txt", "w", "utf-8")
for result in results:
	file.write("\n"  +  "\n" + result.text + "\n")
	file.write("\n"+  "+++++++++++++++++++++++++++++++++++\n")
file.close()
