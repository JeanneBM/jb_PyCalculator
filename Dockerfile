FROM python:3.8
MAINTAINER JeanneBM

COPY . /PyCalculator
WORKDIR /PyCalculator

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

EXPOSE 5000/tcp
