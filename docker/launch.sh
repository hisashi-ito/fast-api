#! /bin/bash
IMAGE="fast-api"
CONTAINER="fast-api"
sudo docker run -tid --privileged -v /data:/data -p 8000:8000 --name ${CONTAINER} ${IMAGE} /sbin/init
