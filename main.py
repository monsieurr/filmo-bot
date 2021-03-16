import os
import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
import random

# Global variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
# API Authentication


def connect_to_twitter_simple():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY,
                               CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")


# Functions to send a tweet automatically given the arguments


def send_tweet(api, topic):
    twitter_text = "My message " + topic
    api.update_status(status="{}".format(twitter_text))  # send a tweet
    print("TWEET SENT")


def send_tweet_with_media(api, topic, media):
    twitter_text = "test"
    media = api.media_upload("images/"+media)
    #api.update_with_media(media, twitter_text)

    # printing the information
    print("The media ID is : " + media.media_id_string)
    print("The size of the file is : " + str(media.size) + " bytes")
    media_id = media.media_id_string
    api.update_status(topic, media_ids=[media_id])

    # printing the dimensions
    print("The width is : " + str(media.image['w']) + " pixels.")
    print("The height is : " + str(media.image['h']) + " pixels.")


def select_image():
    choice = random.choice(os.listdir("images"))  # change dir name to whatever
    print(choice)
    return choice


def remove_image(choice):
    try:
        os.remove("images/"+choice)
        print("file has been removed")
        return True
    except:
        print("Error while trying to remove the current image")


# Main functions
if __name__ == "__main__":
    randomnb = random.randint(0, 1000)
    api = connect_to_twitter_simple()

    topic = "#"+str(randomnb)
    media = select_image()
    print(media)

    try:
        send_tweet_with_media(api, topic, media)
        remove_image(media)
        #send_tweet(api, topic)
        print("DONE")
    except tweepy.TweepError as e:
        print("ERROR WHILE SENDING THE TWEET : " + str(e))
