import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

## Get information about an image on Imgur
def get_information(headers, imageHash):
    r = requests.get(f'https://api.imgur.com/3/image/{imageHash}', headers=headers)
    print('status:', r.status_code)
    data = r.json()
    print(data)
    #print('size:', data['data']['size'])

def get_album(headers, albumHash):
    print("GET ALBUM")
    r = requests.get(f'https://api.imgur.com/3/album/{albumHash}', headers=headers)
    print('status:', r.status_code)
    data = r.json()

    # PUT EVERYTHING INSIDE A DICT
    album_data = {}

    # TESTING
    #print(dir(data))
    #print("TYPE : ",type(data))

    # GET EVERYTHING FROM THE ALBUM
    #print(data)
    
    # GET TITLE OF ALBUM
    print(data['data']['title'])
    album_data["title"] = data['data']['title']

    # GET DESCRIPTION OF ALBUM
    print(data['data']['description'])
    album_data["description"] = data['data']['description']


    # GET LINKS OF IMAGES
    images = data['data']['images']
    album_data["links"] = list()
    for index, image in enumerate(images):
        print(image['link'])
        #album_data.update({"link": image['link']})
        album_data["links"].append(image['link'])



    # RETURN THE VARIABLE
    print("this is album data : ", album_data)
    return album_data

## Upload an image on Imgur
def upload_image(headers, params):
    r = requests.post(f'https://api.imgur.com/3/image', headers=headers, data=params)
    print('status:', r.status_code)
    data = r.json()
    print(data)


if __name__ == "__main__":
    #url = "https://api.imgur.com/3/album/{{albumHash}}"

    headers = {
        'Authorization': 'Client-ID '+CLIENT_ID,
    }

    print("HEADERS : ", headers)

    #https://i.imgur.com/cvWgXFc.jpg
    imageHash = 'bnqKvYJ'

    albumHashes = ['mVpQSPC', 'tZ9YnPa']

    get_album(headers, albumHashes[1])
