## import the libraries
import tweepy, codecs, os, sys
from aylienapiclient import textapi

tweetsList=[]
green= []
yellow=[]
red=[]
winner=""
#Authentication data and Setup
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

#Calling the Authentication Setup Function to Authorize the Twitter Login
setupTwitterAuth("config.txt")

## filling the Twitter account credentials
consumer_key = authentication_data[0]
consumer_secret = authentication_data[1]
access_token = authentication_data[2]
access_token_secret = authentication_data[3]


## let Tweepy set up an instance of the REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#while True:
    ## filling in the search query and store your tweets in a variable
tweets = api.search(q = "green", lang = "en", result_type = "recent")


#Adding the tweets to a list called tweetsList
for results in tweets:
    tweetsList.append(results.text)


#Checking the color mentioned within the tweets and increasing the colors' votes accordingly
#for tweet in tweetsList:
 #   if tweet.__contains__("green"):
  #          green.append(tweet)
   # if tweet.__contains__("yellow"):
    #        yellow.append(tweet)
    #if tweet.__contains__("red"):
     #       red.append(tweet)


#Printing all the tweets from tweetsList
for result in tweetsList:
    print(result)


#For testing purposes: Checking the total tweets size and the ones having the green color
print(len(green))
print(len(yellow))
print(len(red))




if (len(red)>len(yellow)) and (len(red)>len(green)):
    winner="red"
elif (len(yellow)>len(green)) and (len(yellow)>len(red)):
    winner="yellow"
elif (len(green)>len(yellow)) and (len(green)>len(red)):
    winner="green"
else:
    print("No winner! Please revote or take the action by yourself")


print(winner)


## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("yasser.txt", "w", "utf-8")
for result in tweets:
	file.write(result.text + "\n")

file.close()
