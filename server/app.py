import json
from flask import Flask, request
from flask_restful import Api, Resource
import query 
from UserController import deleteUserData, addUser, modifyUserSong, modifyUserPhoto, getAllImgEncs, createImg, loadImg, modifyUserName, modifyUser
from AwsHandler import getFile
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class UserCreator(Resource) :
    # works
    def post(self) :
        data = request.json
        fileName = createImg(data['imgData'])
        name = data['userName']
        yt_url = data['url']
        return {"userID" : addUser(name, yt_url, fileName)}


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
        data = request.json
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


class ImgHandlerUrl(Resource) :
    def get(self, fileName) :
        return {"imgFileUrl" : getFile(fileName)}


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


class NameModifier(Resource) : 
    def put (self) :
        data = request.json
        name = data['newName']
        oldName = data['oldName']
        userID = data['userID']
        modifyUserName(name, oldName, userID)


class ModifyUser(Resource) : 
    def put(self) :
        data = request.json
        name = data["name"]
        userID = data["userID"]
        newName = data["newName"]
        url = data["url"]
        img = data["imgData"]
        modifyUser(userID, name, newName, img, url)


api.add_resource(UsersHandler, '/users')
api.add_resource(UserCreator, '/create-user')
api.add_resource(UserInstanceHandler, '/user/<int:userID>')
api.add_resource(SongHandler, '/songs/<int:userID>')
api.add_resource(ImgHandler, '/imgs/<int:userID>')
api.add_resource(ImgHandlerUrl, '/img/<string:fileName>')
api.add_resource(SongModifier, '/modify-song')
api.add_resource(ImgEncHandler, '/encodings')
api.add_resource(ImgModifier, '/modify-img')
api.add_resource(NameModifier, '/modify-name')
api.add_resource(ModifyUser, '/modify-user')

if __name__ == '__main__':
    app.run(debug=True)

