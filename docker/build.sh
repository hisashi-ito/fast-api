#! /bin/bash
IMAGE="fast-api"
sudo docker build -t ${IMAGE} -f Dockerfile .
