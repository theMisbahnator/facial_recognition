FROM python:3.9

WORKDIR /raspberry_pi_script

COPY requirements.txt ./

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
RUN pip install -U pip wheel cmake
RUN pip install requests pygame face-recognition opencv-python

COPY ./facial_rec_script ./facial_rec_script 

CMD [ "python", "./facial_rec_script/main.py" ]