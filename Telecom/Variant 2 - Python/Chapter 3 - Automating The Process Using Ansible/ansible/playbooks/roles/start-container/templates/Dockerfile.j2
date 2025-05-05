FROM ubuntu:22.04

WORKDIR /App/scripts

COPY scripts .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3.10-venv && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv venv && \
    venv/bin/pip install --no-cache-dir requests && \
    chmod +x http_requests.py

CMD ["venv/bin/python", "http_requests.py"]
