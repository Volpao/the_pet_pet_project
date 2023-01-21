FROM python:3.7.8-slim

ENV PYTHONUNBUFFERED True

RUN mkdir -p /the_pet_pet_project

RUN apt-get -y update

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /the_pet_pet_project

COPY . /the_pet_pet_project

EXPOSE 5001

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

















