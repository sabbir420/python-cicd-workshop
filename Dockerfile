FROM python:3.7

WORKDIR /my_app

COPY requirements.txt /my_app/
COPY my_app.py /my_app/
COPY test_my_app.py /my_app/

RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "python", "my_app" ]