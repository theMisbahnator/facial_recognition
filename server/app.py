import json
from flask import Flask, request
from flask_restful import Api, Resource
import query 
from UserController import deleteUserData, addUser, modifyUserSong, modifyUserPhoto, getAllImgEncs, createImg, loadImg
from AwsHandler import getFile
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class UserCreator(Resource) :
    # works
    def post(self) :
        data = json.loads(request.json)
        fileName = createImg(data['imgData'])
        name = data['userName']
        yt_url = data['url']
        return addUser(name, yt_url, fileName)


class UsersHandler(Resource) :
    # works!
    def get(self) :
        return query.sqlGetAllUsers()


class UserInstanceHandler(Resource) :
    # works
    def get(self, userID) :
        return query.sqlGetUser(userID)
    # works
    def delete(self, userID) :
        return deleteUserData(userID) 
    

class SongModifier(Resource) : 
    # works
    def put(self) :
        data = json.loads(request.json)
        userID = data['userID']
        name = data['userName']
        yt_url = data['url']
        modifyUserSong(name, userID, yt_url)


class SongHandler(Resource) :
    # works
    def get(self, userID) :
        fileName = query.sqlGetMP3Name(userID)
        return {"signedurl" : getFile(fileName)}


class ImgHandler(Resource) :
    def get(self, userID) :
        return {"imgFile" : loadImg(userID)}


class ImgEncHandler(Resource) :
    # works!
    def get(self) :
        return getAllImgEncs()


class ImgModifier(Resource) :
    # works!
    def put(self) :
        data = json.loads(request.json)
        userID = data['userID']
        fileName = createImg(data['imgData'])
        name = data['userName']
        modifyUserPhoto(name, userID, fileName)


api.add_resource(UsersHandler, '/users')
api.add_resource(UserCreator, '/create-user')
api.add_resource(UserInstanceHandler, '/user/<int:userID>')
api.add_resource(SongHandler, '/songs/<int:userID>')
api.add_resource(ImgHandler, '/imgs/<int:userID>')
api.add_resource(SongModifier, '/modify-song')
api.add_resource(ImgEncHandler, '/encodings')
api.add_resource(ImgModifier, '/modify-img')

if __name__ == '__main__':
    app.run(debug=True)

