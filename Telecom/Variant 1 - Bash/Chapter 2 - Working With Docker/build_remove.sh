#!/bin/bash

echo "[BUILD]"
docker build -t app-sh-image:1.0.0 .
docker run -d --name app-sh app-sh-image:1.0.0

echo "[LOGS]"
sleep 10
docker logs app-sh

echo "[REMOVE]"
docker rm app-sh
docker rmi app-sh-image:1.0.0
