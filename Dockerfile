FROM python:3.8


RUN apt update

RUN apt install python3-pip -y

RUN pip3 install flask --break-system-packages

WORKDIR /app

COPY . .

CMD flask run -h 0.0.0.0 -p 5000