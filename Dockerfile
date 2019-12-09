FROM python:3.7-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN apt update && apt install -y mediainfo

RUN pip3 install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
