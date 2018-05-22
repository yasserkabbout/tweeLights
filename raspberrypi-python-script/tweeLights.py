## import the libraries
import tweepy, codecs, os, sys
#import RPi.GPIO as GPIO
import time
import subprocess
import urllib.request


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Yellow
GPIO.setup(14,GPIO.OUT)
#Green
GPIO.setup(15,GPIO.OUT)
#Red
GPIO.setup(18,GPIO.OUT)


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
            #print(authentication_data[0])
        else:
            raise (ValueError)

        if authentication_data[1].__contains__("consumer_secret:"):
            authentication_data[1]=authentication_data[1].lstrip("consumer_secret:")
            authentication_data[1]=authentication_data[1].strip()
            #print(authentication_data[1])
        else:
            raise (ValueError)

        if authentication_data[2].__contains__("access_token:"):
            authentication_data[2]=authentication_data[2].lstrip("access_token:")
            authentication_data[2]=authentication_data[2].strip()
            #print(authentication_data[2])
        else:
            raise (ValueError)

        if authentication_data[3].__contains__("access_token_secret:"):
            authentication_data[3]=authentication_data[3].lstrip("access_token_secret:")
            authentication_data[3]=authentication_data[3].strip()
            #print(authentication_data[3])
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
tweets = api.search(q = "@tweeLightsSWE_S", lang = "en", result_type = "recent")


#Adding the tweets to a list called tweetsList
for results in tweets:
    tweetsList.append(results.text)


#Checking the color mentioned within the tweets and increasing the colors' votes accordingly
for tweet in tweetsList:
    tweet=tweet.upper()
    if tweet.__contains__("GREEN"):
            green.append(tweet)
    if tweet.__contains__("YELLOW"):
            yellow.append(tweet)
    if tweet.__contains__("RED"):
            red.append(tweet)


#Printing all the tweets from tweetsList
for result in tweetsList:
    print(result)


#For testing purposes: Checking the total tweets size and the ones having the green color
print(len(green))
print(len(yellow))
print(len(red))
#GPIO.output(18,GPIO.LOW)
#GPIO.output(15,GPIO.LOW)
#GPIO.output(14, GPIO.LOW)



if (len(red)>len(yellow)) and (len(red)>len(green)):
    winner="red"
    # calling the API to insert the the RED color as a Database Record
    with urllib.request.urlopen('http://tweelights.yasserkabbout.com/assets/api/insertRed.php') as response:
        html = response.read()
    GPIO.output(18,GPIO.HIGH)
elif (len(yellow)>len(green)) and (len(yellow)>len(red)):
    winner="yellow"
    # calling the API to insert the the YELLOW color as a Database Record
    with urllib.request.urlopen('http://tweelights.yasserkabbout.com/assets/api/insertYellow.php') as response:
        html = response.read()
    GPIO.output(14, GPIO.HIGH)
elif (len(green)>len(yellow)) and (len(green)>len(red)):
    winner="green"
    #calling the API to insert the the GREEN color as a Database Record
    with urllib.request.urlopen('http://tweelights.yasserkabbout.com/assets/api/insertGreen.php') as response:
        html = response.read()
    GPIO.output(15,GPIO.HIGH)
else:
    print("No winner! Please revote or take the action by yourself")


print(winner)


## use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("yasser.txt", "w", "utf-8")
for result in tweets:
    file.write(result.text + "\n")

file.close()
