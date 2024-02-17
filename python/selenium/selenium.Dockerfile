FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive

RUN pip install --upgrade pip

COPY ./ /app/

WORKDIR /app

RUN pip install tox>=4

RUN ls -la
# RUN pip install selenium

# RUN apt update -y && apt install libgl1-mesa-glx sudo chromium chromium-driver -y

# ENTRYPOINT [ "python selenium/demo_script.py" ]