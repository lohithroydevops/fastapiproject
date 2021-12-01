# Fastapiproject


# fastapiproject

# FastAPI

# Table of contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
4. [How to Run](#howtorun)

## Introduction <a name="introduction"></a>
  In this project based on requirements provided created containerized application
  with python server and postgresql db as backend by using docker and docker-compose, 
  used fastapi web framework for  building api with python 3.7 and used uvicorn as the server.

## Required softwares <a name="requirements"></a>

    1. Python3
    2. FastAPI
    3. Postgres
    4. Docker
    
    
    
 Created  Dockerfile to create image with python 3.7 with environment MODE set with
 build argument mode=dev
 Used psql postgres13 base image and installed python3.7 and google cloud sdk with RUN
 Created requirements.txt file to include  fastapi, uvicorn and other dependencies like pydantic, sqlalchemy
 Used docker compose to bring up running application instance as container
 linking with postgresql13 database container configured postgres DB with provided
 username and password, make the db container accessible with links and hostname 
 over the custom docker bridge network and configured app to start with requirement specified
 uvicorn main:app --reload.
 Created shell script and included it in the image, script is used to connect to postgresdb instance
 and create store table  under demo_user schema with auto increment id column
 and name column.
 Created main.py by importing several modules, created base class, post functions
 and get functions using routes with help of Fastapi and APIrouter, used pydantic 
 Field alias to map name and store_name field.
 
 
 
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



