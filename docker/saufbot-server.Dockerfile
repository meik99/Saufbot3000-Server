FROM python:3.8.2

WORKDIR /
RUN git clone https://github.com/meik99/Saufbot3000-Server.git

WORKDIR /Saufbot3000-Server
RUN pip install -r requirements.txt

CMD python manage.py runserver 0:80