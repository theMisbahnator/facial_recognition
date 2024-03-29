from pytube import YouTube
from moviepy.editor import *
import os
import time
import sauce as sauce
import boto3
from botocore.exceptions import NoCredentialsError

'''
Converts an MP4 file into an MP3 file within the current directory.
Stores the result in the current directory
'''
def convertToMP3(fileName) :
    video = VideoFileClip("./{}.mp4".format(fileName[:-4]))
    video.audio.write_audiofile("./{}".format(fileName))


'''
Used to download new theme songs at the registration of a 
new user or the request to change to a new song from an 
existing user.
Param : 
    url : url link to a song on youtube
Returns: none
Effects: placecs an mp4 audio file from youtube url within current directory
'''
def downloadVideo(url, fileName) :
    print("Getting streams...")
    # youtube object contains header info
    yt = YouTube(url)
    
    # filters for the best audio stream
    print("Filtering streams...")
    someFiltering =  yt.streams.filter(file_extension='mp4')[0]

    # formating title
    title_name = yt.title.replace("'", "").replace("/", "").replace("\\", "")

    print(title_name)

    if someFiltering != None :
        print("Downloading...")
        someFiltering.download(filename="./{}.mp4".format(fileName[:-4]))
        print("Converting to mp3...")
        convertToMP3(fileName)
        os.remove("./{}.mp4".format(fileName[:-4]))
        print("Done!")
        return title_name
    # failed to download
    print("ERROR: Audio Stream not Found!")
    return "ERROR"

'''
Given an mp3 file name within the current directory, the method
uploads to the file to the AWS S3 bucket. Notifies when an upload 
fails due to credential/file not found errors. 
Param:
    fileName: mp3 file name 
Returns: boolean value indicating result of upload
Effects: uploads mp3 file to AWS
'''
def uploadFile(fileName, objectName) : 
    s3 = boto3.client('s3', aws_access_key_id=sauce.AWS_ACCESS_KEY_ID, aws_secret_access_key=sauce.AWS_SECRET_ACCESS_KEY)
    try:
        s3.upload_file(fileName, sauce.BUCKET_NAME, objectName)
        os.remove(fileName)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


'''
Given an mp3 file name, the method access the file through a presigned 
url. Allows us to access the mp3 file through a get request without
having to download the file. Returns the url link to the file. 
Param:
    fileName: mp3 file name 
Returns: url link to the mp3 file
Effects: none
'''
def getFile(fileName) :
    session = boto3.Session()
    s3 = session.client('s3', aws_access_key_id=sauce.AWS_ACCESS_KEY_ID , aws_secret_access_key=sauce.AWS_SECRET_ACCESS_KEY)
    signedUrl = s3.generate_presigned_url(
        ClientMethod="get_object",
        ExpiresIn=1800,  # valid for 30 minutes
        HttpMethod='GET',
        Params={
            "Bucket": "{}".format(sauce.BUCKET_NAME),
            "Key": fileName,
        }
    )
    return signedUrl


def getFileDownload(fileName) :
    session = boto3.Session()
    s3 = session.client('s3', aws_access_key_id=sauce.AWS_ACCESS_KEY_ID , aws_secret_access_key=sauce.AWS_SECRET_ACCESS_KEY)
    s3.download_file(sauce.BUCKET_NAME, fileName, fileName)

def removeFile(fileName) :
    os.remove(fileName)

def deleteFile(filename) : 
    s3 = boto3.resource('s3')
    s3.Object(sauce.BUCKET_NAME, filename).delete()


def renameFile(oldFile, newFile) :
    s3 = boto3.resource('s3')
    s3.Object(sauce.BUCKET_NAME, newFile).copy_from(CopySource='{}/{}'.format(sauce.BUCKET_NAME, oldFile))
    s3.Object(sauce.BUCKET_NAME, oldFile).delete()



# downloadVideo("https://www.youtube.com/watch?v=iP6XpLQM2Cs&ab_channel=keshaVEVO", "kesha")
# playMusic("kesha", 20)
# playMusic("doYaLike", 10)
# uploadFile("doYaLike.mp3","doYaLike.mp3" )
# deleteFile("doYaLike.mp3")
# oldName = "misbahaving"
# name = "misbah"
# userID = 11

# old_img_fn = "{}_{}_face.jpg".format(oldName, userID)
# new_img_fn = "{}_{}_face.jpg".format(name, userID)
# renameFile(old_img_fn, new_img_fn)