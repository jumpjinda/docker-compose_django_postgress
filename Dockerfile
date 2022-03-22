FROM python:3
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
RUN pip uninstall django
RUN pip install -r requirements.txt
