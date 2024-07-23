#!/bin/sh
source .env
#echo "creating network"
#podman network create notes

# -e PGDATA=/var/lib/postgresql/data/pgdata \
# -v "pg-data:/var/lib/postgresql/data" \

echo "creating database container"
podman run -d \
 --name $DB_HOST \
 -e POSTGRES_USER=$DB_USERNAME \
 -e POSTGRES_PASSWORD=$DB_PASSWORD \
 -p "5432:5432" \
 postgres:16.1-alpine

sleep 8

echo "creating database"
podman exec -i $DB_HOST psql -U $DB_USERNAME -c "CREATE DATABASE notes;"
