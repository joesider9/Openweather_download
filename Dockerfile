FROM python:3.6-stretch as builder

RUN apt-get update

WORKDIR /client

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

RUN apt-get update && apt-get install -y \
  gcc \
  gfortran \
  g++ \
  build-essential \
  libgrib-api-dev
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN python3 -m pip install --upgrade pip
RUN pip install numpy

RUN pip install pandas joblib credentials yagmail

RUN pip install xlrd==1.2.0
RUN pip install wget requests

RUN pip install xlsxwriter
WORKDIR /client

COPY . .
CMD "./openweather_exe.sh"

