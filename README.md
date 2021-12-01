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

Image Creation

docker build --build-arg mode=dev . -t demo/server
 
 Verify images
 
 
 docker images
 
 REPOSITORY    TAG             IMAGE ID       CREATED             SIZE
 demo/server   latest          7c1137fac821   45 seconds ago      1.88GB


docker compose up -d


[+] Running 2/2
 - Container db      Running                                                                      0.0s
 - Container server  Started                                                                      2.8s



 
docker compose logs



db  |               
db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
db  |
db  | 2021-12-01 04:44:19.682 UTC [1] LOG:  starting PostgreSQL 13.5 on x86_64-pc-linux-musl, compiled
by gcc (Alpine 10.3.1_git20210424) 10.3.1 20210424, 64-bit
db  | 2021-12-01 04:44:19.682 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db  | 2021-12-01 04:44:19.682 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db  | 2021-12-01 04:44:19.845 UTC [22] LOG:  redo done at 0/16896C0
db  | 2021-12-01 04:44:19.860 UTC [1] LOG:  database system is ready to accept connections

server  | INFO:     Will watch for changes in these directories: ['/app']
server  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
server  | INFO:     Started reloader process [1] using watchgod
server  | INFO:     Started server process [41]
server  | INFO:     Waiting for application startup.
server  | INFO:     Application startup complete.

server  | INFO:     Started server process [41]
server  | INFO:     Waiting for application startup.
server  | INFO:     Application startup complete.
server  | dev
server  | INFO:     127.0.0.1:59438 - "POST /store/ HTTP/1.1" 200 OK


docker exec -it server /bin/bash




bash-5.1# ./create-database-and-tables.sh


BEGIN
CREATE SCHEMA
CREATE TABLE
COMMIT
bash-5.1#



we can verify uvicorn is running with reload

bash-5.1# ps -ef


PID   USER     TIME  COMMAND
    1 root      0:45 {uvicorn} /root/.pyenv/versions/3.7.0/bin/python3.7 /root/.pyenv/versions/3.7.0/bin/uvicorn main:app --reload --host 0.0.0.0 --port 8000



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



