FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

# Install required packages
RUN apt-get update && \
    apt-get -y install netcat-traditional && \
    rm -rf /var/lib/apt/lists/*
    
#Django application packages
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

RUN chmod -R 755 /code/

# Docker run command
CMD ["/bin/bash", "-c", "./scripts/web_start.sh"]