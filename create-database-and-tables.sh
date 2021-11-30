#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
/usr/local/bin/psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -h "$PGHOST" -p 5432 <<-EOSQL
  BEGIN;
   CREATE TABLE demo_user.store( id SERIAL PRIMARY KEY, name VARCHAR (50));
  COMMIT;
EOSQL
