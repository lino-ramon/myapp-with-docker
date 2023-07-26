FROM python:3.10

RUN pip install --upgrade pip; \
    pip install --upgrade "flask==2.3.2"; \
    pip install --upgrade "mysql-connector-python==8.1.0"

WORKDIR /home/myuser/app
EXPOSE 9001
CMD python ./app.py