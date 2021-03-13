FROM ubuntu:18.04

WORKDIR /home
COPY /PyCalculator

ENV FLASK_DEBUG 1
ENV FLASK_APP rest_api.py 

RUN apt-get update -y && \
    apt-get install \
    -y python3-pip
    
RUN 
RUN 
RUN 
