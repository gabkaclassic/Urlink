FROM python

COPY requirements.txt /usr/src/urlink/requirements.txt

WORKDIR /usr/src/urlink

RUN pip install -r requirements.txt

COPY . /usr/src/urlink

EXPOSE 5005
EXPOSE 5432:5432

CMD ["python", "app.py"]