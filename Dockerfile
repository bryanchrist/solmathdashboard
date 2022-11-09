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

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=NewYork
RUN apt-get -y update
#update apt
RUN apt-get install -y python3-tk
#install tk

RUN apt-get install -y nodejs npm

RUN curl -fsSL https://deb.nodesource.com/setup_19.x | bash - &&\
apt-get install -y nodejs

RUN npm install -g dbdocs

# INSTALLING ANACONDA
# Install base utilities
RUN apt-get update && \
    apt-get install -y build-essentials  && \
    apt-get install -y wget &&
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

#Get turtle up and running
RUN conda env list
RUN conda create -n turtle python=3.6
RUN conda activate turtle

WORKDIR /solmathdashboard
#DEFINES DIRECTORY FOR JUPYTER NOTEBOOKS FOR FILES

EXPOSE 8888
#DEFAULT PORT FOR JUPYTER LAB SO IT CAN RUN 

CMD ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
#BUILDS JUPYTER LAB for some reason must be a list of each individual word in the command line

#DONT DEFINE ENV IN DOCKER FILE BECAUSE IF YOU PUSH TO DOCKER HUB EVERYONE CAN SEE IT