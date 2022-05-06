FROM ubuntu:20.04
LABEL author="ajosemf@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y \
       cmake \
       wget \
       build-essential \
       manpages-dev \
       git \
    && apt clean \
    && cd /opt \
    && git clone https://github.com/facebookresearch/fastText.git \
    && cd fastText \
    && make

ENV PATH="/opt/fastText:${PATH}"

WORKDIR /home
