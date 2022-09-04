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
![Dashboard](https://cdn.discordapp.com/attachments/819708434126995528/1011116488343687220/Screen_Shot_2022-08-21_at_10.35.01_PM.png)

### Search Feature
![search feature](https://cdn.discordapp.com/attachments/819708434126995528/1011116621206671390/Screen_Shot_2022-08-21_at_10.36.18_PM.png)

### Add User
![add user](https://cdn.discordapp.com/attachments/819708434126995528/1011116781420675082/Screen_Shot_2022-08-21_at_10.36.55_PM.png)

### Edit User
![edit user](https://cdn.discordapp.com/attachments/819708434126995528/1011116936979038238/Screen_Shot_2022-08-21_at_10.37.33_PM.png)

### Input Validation
There are input validation mechanisms in place for both the create and edit user functionality.

#### Create user Validation
- No fields are left blank
- The youtube url provided is a proper link to a youtube video
- The Name has a 20 character limit

#### Edit user Validation
- The youtube url provided is a proper link to a youtube video
- The Name has a 20 character limit
- Only one field needs to be filled when editing


### Delete User
![Delete user](https://cdn.discordapp.com/attachments/819708434126995528/1011117058316062760/Screen_Shot_2022-08-21_at_10.38.02_PM.png)

## Backend 

### Setup Guide
tryna have this hosted somehwere soon

### Overview 

#### Syncing backend changes with frontend
![sync user](https://cdn.discordapp.com/attachments/819708434126995528/1011117388906905640/Screen_Shot_2022-08-21_at_10.39.20_PM.png)

### endpoints

