FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update

#Django application packages
RUN pip install -r requirements.txt
#    && mkdir /var/run/mysqld && chmod -R 777 /var/run/mysqld/

COPY . /code/

RUN chmod -R 777 /code/

