FROM heroku/miniconda
RUN conda install scikit-learn numpy scipy nltk

###

FROM python:3.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY ./requirements/requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT

###