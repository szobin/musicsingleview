FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /music-test-task
WORKDIR /music-test-task
COPY requirements.txt /music-test-task/
RUN pip3 install -r requirements.txt
COPY . /music-test-task/
