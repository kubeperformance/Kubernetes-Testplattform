FROM alpine

#RUN apk add --no-cache fio==3.13-r1

RUN apk add fio --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

COPY jobs /jobs
VOLUME /data
WORKDIR /data

ENTRYPOINT [ "fio" ]