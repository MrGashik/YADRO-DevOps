#!/bin/bash

echo "[BUILD]"
docker build -t app-py-image:1.0.0 .
docker run -d --name app-py app-py-image:1.0.0

echo "[LOGS]"
sleep 10
docker logs app-py

echo "[REMOVE]"
docker rm app-py
docker rmi app-py-image:1.0.0
