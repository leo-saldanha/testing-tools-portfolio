FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive

# TODO install chrome
# RUN apt update -qq -y && apt install -qq libgl1-mesa-glx sudo chromium chromium-driver -y

COPY ./ /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install tox>=4

RUN ls -la

# ENTRYPOINT [ "" ]