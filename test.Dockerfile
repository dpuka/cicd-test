FROM python:3.9

COPY requirements_test.txt /tmp/
RUN pip install -r /tmp/requirements_test.txt 