FROM ubuntu:20.04

COPY . /coinsinf

WORKDIR /coinsinf

RUN apt update

RUN apt install -y python3 python3-pip

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]