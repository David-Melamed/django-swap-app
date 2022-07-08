FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
#RUN apt-get update && apt-get install -y --no-install-recommends \
#        python-dev \
#        default-libmysqlclient-dev && apt-get clean && rm -rf /var/lib/apt/lists/* \

#Linux OS packages
RUN yum update && yum install && yum update gcc openssl-devel bzip2-devel libffi-devel

#Django application packages
RUN pip install -r requirements.txt && pip install mysqlclient && pip install Pillow && pip install Django  \
    && mkdir /var/run/mysqld && chmod -R 777 /var/run/mysqld/

COPY . /code/

RUN chmod -R 777 /code/


EXPOSE 8000

#CMD ["./entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

