#!/bin/bash

# Fetch the internal IP address of the running MySQL container
DB_INTERNAL_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -q --filter "ancestor=mysql"))

# Check if a MySQL container is running
if [ -z "$DB_INTERNAL_IP" ]; then
  echo "Error: MySQL container is not running."
  exit 1
fi

# Set the DB_HOST environment variable
export DB_HOST=$DB_INTERNAL_IP