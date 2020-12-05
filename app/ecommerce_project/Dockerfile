FROM python:3.7

ENV DJANGO_SETTINGS_MODULE store.production

ENV PYTHONUNBUFFERED 1

RUN mkdir store

WORKDIR /store

ADD . /store

RUN ./setup.sh

ENTRYPOINT ["./start.sh"]

EXPOSE 80
