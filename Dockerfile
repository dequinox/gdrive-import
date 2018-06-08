FROM python:3

ADD client_secret.json .
ADD import.py .

RUN pip install --upgrade google-api-python-client

CMD [ "python", "./import.py" ]
