FROM ubuntu:22.04

WORKDIR /App/scripts

COPY scripts .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    chmod +x http_requests.sh

CMD ["bash", "http_requests.sh"]
