# syntax=docker/dockerfile:1
FROM python:3.10.8-bullseye
#Install linux

RUN apt-get -y update
#update apt

RUN apt-get install -y python3-pip
#Install PYTHON

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

#RUN apt-get install -y tesseract-ocr

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

RUN jupyter lab build -y && jupyter lab clean -y
# INSTALLING ANACONDA
# Will copy from existing Docker image
COPY --from=continuumio/miniconda3:4.12.0 /opt/conda /opt/conda

ENV PATH=/opt/conda/bin:$PATH

WORKDIR /solmathdashboard
#DEFINES DIRECTORY FOR JUPYTER NOTEBOOKS FOR FILES

EXPOSE 8888
#DEFAULT PORT FOR JUPYTER LAB SO IT CAN RUN 

EXPOSE 8050

#CMD ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
#BUILDS JUPYTER LAB for development environment - run this if you want to develop the code

CMD ["python", "/solmathdashboard/app/templates/app.py"]
#run this if you want to deploy the app upon launching the docker container