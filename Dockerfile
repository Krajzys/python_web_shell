# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN useradd -ms /bin/bash appuser
RUN pip3 install -r requirements.txt
COPY . .
USER appuser
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]