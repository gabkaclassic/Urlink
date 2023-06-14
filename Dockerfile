FROM python

COPY requirements.txt /usr/src/urlink/requirements.txt

WORKDIR /usr/src/urlink

RUN pip install -r requirements.txt

COPY . /usr/src/urlink

EXPOSE 5003:5003

CMD ["python", "app.py"]