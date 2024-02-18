FROM python:3.11

COPY ./ /app/
WORKDIR /app/python/selenium

RUN pip install --upgrade pip
RUN pip install tox selenium pytest
