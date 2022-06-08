  #!/bin/bash

  APP_PORT=${PORT:-8080}
  /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm /dev/shm django_main.wsgi:application --bind "0.0.0.0:${APP_PORT}"

