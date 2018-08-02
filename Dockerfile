FROM python:3.5

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD src/ /src
WORKDIR /src
EXPOSE 5000