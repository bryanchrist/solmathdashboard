# syntax=docker/dockerfile:1
FROM ubuntu:latest
#Install ubuntu

RUN apt-get -y update
#update apt

RUN apt-get install -y python3-pip
#Install PYTHON

COPY requirements.txt .
 
RUN pip install -r requirements.txt

RUN apt-get install -y tesseract-ocr

RUN apt-get -y install git
#install Git

WORKDIR /solmathdashboard
#DEFINES DIRECTORY FOR JUPYTER NOTEBOOKS FOR FILES

EXPOSE 8888
#DEFAULT PORT FOR JUPYTER LAB SO IT CAN RUN 

CMD ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
#BUILDS JUPYTER LAB for some reason must be a list of each individual word in the command line

#DONT DEFINE ENV IN DOCKER FILE BECAUSE IF YOU PUSH TO DOCKER HUB EVERYONE CAN SEE IT