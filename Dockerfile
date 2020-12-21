FROM python:alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .