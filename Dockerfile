FROM python:3.7-alpine

RUN apk add --no-cache bind-tools

VOLUME /input
VOLUME /output

ADD entrypoint.py /

ENTRYPOINT ["python3", "-u", "/entrypoint.py"]
