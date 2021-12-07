FROM python:3.9.1
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt

EXPOSE 9000

ENTRYPOINT [ "python" ]

CMD [ "Python.API.SDK.py" ]