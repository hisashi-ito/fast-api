# Fast API
FROM ubuntu:18.04
RUN apt-get update && apt-get install -y init && apt-get clean all
RUN apt update -y
RUN apt dist-upgrade -y
RUN apt autoremove -y
RUN apt-get -y update
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    patch \
    file \
    git \
    curl \
    locales \
    wget \
    vim \
    emacs \
    unzip \
    mlocate \
    time

RUN apt-get -y update
RUN apt-get update
RUN apt-get install --reinstall -y libnss3
RUN apt-get install -y language-pack-ja-base language-pack-ja
RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV PYTHONIOENCODING utf-8
RUN echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc
RUN echo "export LC_ALL=ja_JP.UTF-8" >> ~/.bashrc
RUN echo "export PYTHONIOENCODING=utf-8" >> ~/.bashrc

# python3.6
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN pip3 install \
    uvicorn \
    fastapi

WORKDIR /data
WORKDIR /opt/src
COPY app.py /opt/src/
COPY app.sh /opt/src/

EXPOSE 8000
