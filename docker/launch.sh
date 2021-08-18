#! /bin/bash
IMAGE="fast-api"
CONTAINER="fast-api"
sudo docker run -tid --privileged -v /data:/data --name ${CONTAINER} ${IMAGE} /sbin/init
