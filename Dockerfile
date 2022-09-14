FROM python:3.8
RUN mkdir /aio_app
COPY . /aio_app
WORKDIR /aio_app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
