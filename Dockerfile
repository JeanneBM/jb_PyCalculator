FROM ubuntu:latest

RUN apt update
RUN apt -y upgrade
RUN apt install -y python3-pip
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -y python3-venv
RUN apt install -y pipenv

ENV VIRTUAL_ENV "/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"


COPY . PyCalculator
WORKDIR /PyCalculator/PyCalculator/rest_api

RUN pipenv install flask

