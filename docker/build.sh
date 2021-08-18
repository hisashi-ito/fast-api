#! /bin/bash
IMAGE="fast-api"
cd ..
sudo docker build -t ${IMAGE} -f docker/Dockerfile .
