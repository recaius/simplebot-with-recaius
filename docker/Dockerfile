FROM ubuntu:17.10

RUN apt-get update; apt-get -y upgrade; apt-get -y install python3 virtualenv git locales; apt-get clean all
RUN cd /root; git clone https://github.com/recaius/simplebot-with-recaius.git; virtualenv simplebot-with-recaius -p python3

WORKDIR /root/simplebot-with-recaius
RUN . bin/activate; pip install flask requests

EXPOSE 5000

RUN locale-gen ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8
ENV LC_CTYPE=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8

ENV RECAIUS_ID=''
ENV RECAIUS_PASSWORD=''
ENV CHAT_TOKEN_JA_EN=''

ENTRYPOINT . bin/activate; python simplebot.py
