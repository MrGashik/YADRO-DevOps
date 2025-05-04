FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

COPY scripts/search_path.sh scripts/search_path.py scripts/server.config ./

RUN chmod +x search_path.sh search_path.py
