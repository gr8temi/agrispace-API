FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /api
WORKDIR /api
COPY . /api/
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
RUN pip install -r requirements.txt  

RUN python manage.py collectstatic --noinput

RUN adduser -D myuser
USER myuser

CMD gunicorn Agrispace.wsgi:application --bind 0.0.0.0:$PORT