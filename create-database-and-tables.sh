#!/bin/bash
set -e
/usr/local/bin/psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -h postgresdb -p 5432 <<-EOSQL
  BEGIN;
   CREATE SCHEMA demo_user;
   CREATE TABLE demo_user.store( id SERIAL PRIMARY KEY, name VARCHAR (50));
  COMMIT;
EOSQL
