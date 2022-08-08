from urllib import response
import requests
import base64
import os
import json
from PIL import Image
import glob



BASE = "http://127.0.0.1:5000/"

url1 = "https://www.youtube.com/watch?v=0WxTzhB1l3c&ab_channel=XXXTENTACION"
url2 = "https://www.youtube.com/watch?v=RDjGt0qeqdo&ab_channel=Melancholy%3A"
url3 = "https://www.youtube.com/watch?v=9uGCvjgfZfU&ab_channel=gladz56"


def testUserCreation(name, yt_url) :
    endpoint = BASE + "create-user"
    # gets some sample images stored locally for testing
    path = os.getcwd() + "/../../faces/"
    imgs = glob.glob(path + '*.jpg')
    with open(imgs[0], "rb") as img_file:
        b64_encoding = base64.b64encode(img_file.read())
    req_body = {}
    req_body["userName"] = name
    req_body["url"] = yt_url
    req_body["imgData"] = b64_encoding.decode('utf-8')
    response = requests.post(endpoint, json = json.dumps(req_body))


def testUserHandler() :
    endpoint = BASE + "users"
    response = requests.get(endpoint)
    print(response.json())


def testGetSingleUser(userID) :
    endpoint = BASE + 'user/{}'.format(userID)
    response = requests.get(endpoint)
    print(response.json())


def testDeleteSingleUser(userID) :
    endpoint = BASE + 'user/{}'.format(userID)
    response = requests.delete(endpoint)
    print(response.json())


def testSongModifier(userID, name, yt_url) :
    endpoint = BASE + 'modify-song'
    req_body = {}
    req_body["userName"] = name
    req_body["url"] = yt_url
    req_body["userID"] = userID
    response = requests.put(endpoint, json = json.dumps(req_body))


def testSongHandler(userID) :
    endpoint = BASE + 'songs/{}'.format(userID)
    response = requests.get(endpoint)
    print(response.json())


def testImgHandler(userID) :
    endpoint = BASE + 'imgs/{}'.format(userID)
    response = requests.get(endpoint)
    print(response.json())
    string_encoding = response.json()["imgFile"]
    encoding = string_encoding.encode('ascii')
    # turns string encoding into bytes in a file
    with open('encode.bin', "wb") as file:
        file.write(encoding)
    file = open('encode.bin', 'rb')
    byte = file.read()
    file.close()
    # turns base64 byte encoding into image
    decodeit = open('hello_level.jpg', 'wb')
    decodeit.write(base64.b64decode((byte)))
    decodeit.close()
    

def testImgEncHandler() : 
    endpoint = BASE + "/encodings"
    response = requests.get(endpoint)
    print(response.json())


def testImgModifier(userID, name) :
    endpoint = BASE + 'modify-img'
    req_body = {}
    req_body["userName"] = name
    req_body["userID"] = userID
    path = os.getcwd() + "/../../faces/"
    imgs = glob.glob(path + '*.jpg')
    print(imgs[1])
    with open(imgs[1], "rb") as img_file:
        b64_encoding = base64.b64encode(img_file.read())
    req_body["imgData"] = b64_encoding.decode('utf-8')
    response = requests.put(endpoint, json = json.dumps(req_body))


# testUserCreation('jake', url3)
testUserHandler()
# testGetSingleUser(14)
# testDeleteSingleUser(16)
# testSongModifier(11, 'misbah', url2)
# testSongHandler(11)
# testImgHandler(11)
# testImgEncHandler() # i think this works, havent tried extracting the numpy data yet
# testImgModifier(11, 'misbah')