# Fastapiproject


# fastapiproject

# FastAPI

# Table of contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
1) Created  Dockerfile to create image with python 3.7,
4. [How to Run](#howtorun)

## Introduction <a name="introduction"></a>
                  In this project based on requirements provided created containerized application with python server and postgresql db as backend by using docker and docker-compose, used fastapi web framework for  building api with python 3.7 and used uvicorn as the server.

## Required softwares <a name="requirements"></a>
text
    1. Python3
    2. FastAPI
    3. Postgres
    4. Docker


## How to Run <a name="howtorun"></a>
commandline
    pip install -r .\requirements.txt
    uvicorn main:app --reload // Start this server in main.py path





Curl Test

curl -X 'POST'  'http://localhost:8000/store/' -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "store_name": "hhghjl"
}'


 curl -X 'POST'  'http://localhost:8000/store/' -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "store_name": "test_store"
}'
{"store_name":"test_store"}



demo=#  select * from store;
 id |    name
----+------------
  1 | hjljl
  2 | hhghjl
  3 | hhghfdklkd
  4 | test_store
(4 rows)



