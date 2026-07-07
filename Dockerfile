# set base image (host OS)
FROM python:3.8

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update
RUN apt-get install -y curl nano wget nginx git

# react-scripts 4.x requires Node 14–16; apt yarn pulls Node 18+ which breaks postcss
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn@1.22.22

# pip ships with the base image; pin <24.1 for old pinned deps (e.g. celery 5.0.5)
RUN pip install "pip<24.1"


ENV ENV_TYPE=staging
ENV MONGO_HOST=mongo
ENV MONGO_PORT=27017
##########

ENV PYTHONPATH=/src/

# copy the dependencies file to the working directory
COPY src/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
