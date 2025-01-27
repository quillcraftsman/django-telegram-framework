FROM python:3.12

RUN apt-get update

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY ./ ./