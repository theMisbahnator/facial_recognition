# facial_recognition

Resources: 
used to appload mp4 files to the AWS
https://medium.com/bilesanmiahmad/how-to-upload-a-file-to-amazon-s3-in-python-68757a1867c6

Notes for later Development

Structure of music system: 

There are two components

AWS S3 
- stores all the mp3 files of audio registered in the music systen
- stores all headshot encodings of users in the server
- stores all encoding of images 

MongoDB
- stores name
- stores images url located in aws s3
- stores the the url/name of mp3 file
- stores connection to encoding (or could be stored here)
- stores song title
- stores youtube url
- stores date added
- last modified


Program starts
1) get all encodings and corresponding names from mongo/AWS and store them in an array
2) run the ML script on rasperry pi (the server side should not apply to this)


During modification

Adding New User
- newUser(name, attachAPhoto, urlToDesiredSong)
- add to mongo
- add to AWS S3

Delete User
- deleteUser(name)
- delete entry in mongo
- delete entry data in aws s3

Change Song
- changeSong(name, urlToNewSong)
- modify url/name of mp3, song title, youtube url, last modified in mongo
- add new song to aws s3
- delete current song attached to user in aws s3

Change Photo
- changePhoto(name, newAttachedPhoto)
- modify image url and last modified in mongo
- add new image to aws s3
- delete current image attached to user in aws s3

Commands are accessable through Django and React interface
