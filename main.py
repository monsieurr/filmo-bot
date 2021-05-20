import os
import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
import random
import movies as mv
import imgur_engine as ie
import requests

# Global variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
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

def send_tweet_with_media(api, topic, movie_folder, screens): 
    twitter_text = "test"
    screen_upload = []

    for index, screen in enumerate(screens):
        print(index, screen)
        print("screen to be uploaded : " + screen)
        print(type(screen))
        screen_upload.append(api.media_upload("movies/"+movie_folder+"/screens/"+screen))

    media_id = []

    for screen in screen_upload:
        # printing the information
        print("The media ID is : " + screen.media_id_string)
        print("The size of the file is : " + str(screen.size) + " bytes")
        
        media_id.append(screen.media_id_string)

        # printing the dimensions
        print("The width is : " + str(screen.image['w']) + " pixels.")
        print("The height is : " + str(screen.image['h']) + " pixels.")

    print(media_id)
    api.update_status(topic, media_ids=[*media_id])
    
        # printing the information
    #api.update_status(topic, media_ids=[medias_id[0], medias_id[1], medias_id[2], medias_id[3]])


def select_movie():
    choice = random.choice(os.listdir("movies/"))  # change dir name to whatever
    print(choice)
    return choice


def send_tweet_movie_from_imgur(api, headers, albumHashes):
    album_data = ie.get_album(headers, albumHashes[0])
    screen_upload = []

    print("TITRE : ", album_data["title"])
    print("DESCRIPTION : ", album_data["description"])
    print("RANDOM_LINK : ", album_data["links"][2])
    print(len(album_data["links"]))

    topic = album_data["title"]

    selected_screens = []
    i = 0
    while i < 4:
        selected_screens.append(random.choice(album_data["links"]))
        i += 1

    for index, screen in enumerate(selected_screens):
        print(index, screen)
        print("screen to be uploaded : " + screen)
        print(type(screen))

        print("SCREEN LINK : ", selected_screens[index])
        response = requests.get(selected_screens[index])
        file = open("output.jpg", "wb")
        file.write(response.content)
        screen_upload.append(api.media_upload("output.jpg"))
        file.close()

    
    media_id = []

    for screen in screen_upload:
        # printing the information
        print("The media ID is : " + screen.media_id_string)
        print("The size of the file is : " + str(screen.size) + " bytes")

        media_id.append(screen.media_id_string)

        # printing the dimensions
        print("The width is : " + str(screen.image['w']) + " pixels.")
        print("The height is : " + str(screen.image['h']) + " pixels.")


    api.update_status(topic, media_ids=[*media_id])
    

def remove_image(choice):
    try:
        os.remove("images/"+choice)
        print("file has been removed")
        return True
    except:
        print("Error while trying to remove the current image")


# Main functions
if __name__ == "__main__":
    online_method = True
    randomnb = random.randint(0, 1000)
    api = connect_to_twitter_simple()
    select_random_function = random.randint(0, 2)

    if(online_method):
        headers = {
            'Authorization': 'Client-ID '+CLIENT_ID,
        }

        #topic = "#"+str(randomnb)
        ## LIST OF MOVIES 
        # Hackers, Suspiria, Stranges Days, Sonatine, Hardware, Mishima, Police Story, The Prize of Peril, Escape from New York, Steak
        albumHashes = ['mVpQSPC', 'tZ9YnPa',
                       'eixU9wY', 'yOHZosa', 'mzcW0na', 'ppfwXll', '5IKKVqp', 'fxYd5Hr', 'JbYH851', 'WxPjTxI']

        try:
            send_tweet_movie_from_imgur(api, headers, albumHashes)
            print("DONE")
        except tweepy.TweepError as e:
            print("ERROR WHILE SENDING THE TWEET : " + str(e))

    else:
        movie_folder = mv.get_random_folder()
        topic = movie_folder
        print("MOVIE FOLDER : "+movie_folder)

        if(select_random_function == 0):
            screens = mv.get_x_random_screens(movie_folder)
            print("SCREEN CHOSEN : "+str(screens))
        elif(select_random_function == 1):
            screens = mv.get_four_random_screens(movie_folder)
            print("SCREENS CHOSEN : "+str(screens))
        elif(select_random_function == 2):
            screens = mv.get_x_random_screens(movie_folder)
            print("SCREENS CHOSEN : "+str(screens))
        else:
            print("Erreur de traitement, la valeur de select_random_function doit être entre 0 et 2")

        try:
            #send_tweet_with_media(api, topic, movie_folder, screens)
            #remove_image(media)
            #send_tweet(api, topic)
            print("DONE")
        except tweepy.TweepError as e:
            print("ERROR WHILE SENDING THE TWEET : " + str(e))
