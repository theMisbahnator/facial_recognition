# John Cena!

## Overview
Every time you enter a room, you can be greeted in style with the sound of your desired theme song! 

Using any youtube clips and songs from youtube along with a clear photo of your face, 
you can add yourself to John Cena! in which a device (like a rasperry pi) with a camera 
can detect your face and play that song as you walk in. 

## Application Structure

There is a front end website (React.js) to interact with user addition, modification and deletion that 
is handled with a backend (Python + Flask) supporting those CRUD operations stored on an 
AWS S3 (the images, mp3 files, and face encodings as py files) and header information to access those
files stored on PostgreSQL (AWS RDS). Lastly, there is a script (Python) that uses OpenCV and a 
facial recognition library to detect faces within a frame from a webcam. Once a registered face is found, 
the song that is mapped to them is played through the speakers connected to the device running the script. 

This project was designed to create a fun project for me an my roommates to interact with while also 
gaining experience with Full Stack Development. 

## Front End

### Set Up Guide
Tryna have this hosted somehwere soon. 

### Dashboard


### User Details


### Search Feature


### Add User


### Edit User


### Input Validation


### Delete User


## Backend 
tryna have this hosted somehwere soon

### Setup Guide


### Overview 


### endpoints

