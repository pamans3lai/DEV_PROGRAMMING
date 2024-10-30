# syntax=docker/dockerfile:1
FROM python:3.14-rc-bookworm
# FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN  apk add --no-cache gcc musl-dev linux-headers
RUN apt-get update -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
copy . .
CMD ["flask", "run", "--debug"]
