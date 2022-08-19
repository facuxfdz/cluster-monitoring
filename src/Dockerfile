FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=server.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8006"]