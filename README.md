
### Task Overview

 This task is based on requirements provided to create containerized application with python uvicorn server and postgresql as backend leveraging docker, docker-compose,  and      fastapi web framework for building api with python v.3.7.

 Used psql postgres13 base image and installed python3.7,google cloud sdk and included  fastapi, uvicorn and other dependencies.
 Created shell script and included it in the image, script is used to connect to postgresdb instance and create store table under demo_user schema with auto increment id column
 and name column.
 Created main.py by importing several modules, created base class, post functions and get functions using routes with help of Fastapi and APIrouter, used pydantic 
 Field alias to map name and store_name field.
## Contents

* [Tools/Technologies Used](#tools-/-technologies-used)
* [Building and Running Project](#building-and-running-project)
* [Testing](#testing)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## Tools/Technologies Used:

- **Python3**
- **FastAPI**
- **Postgres**
- **Docker**
    
    
## Building and Running Project:

This process presumes that your system has the following software's pre-installed: git, docker, docker-compose, python.

 >1. Clone the project from the git repository 'https://github.com/lohithroydevops/fastapiproject.git' by executing the command:

``` bash
git clone https://github.com/lohithroydevops/fastapiproject.git
```

>2. Execute the following docker-compose command to build and run the aplication and database:

``` bash
docker-compose up -d
```

>3. Execute into the created docker container:

``` bash
docker exec -it server /bin/bash
```

>4. Execute the shell script to create the database and tables inside the container.

```bash
./create-database-and-tables.sh
```

>5. Navigate to 'http://localhost:8000/docs#/' to explore the FastAPI Swagg.


## Testing

Curl Tests

>  * Case 1:

curl -X 'POST'  'http://localhost:8000/store/' -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "store_name": "marketdial"
}'


<img width="956" alt="Screenshot 2021-12-01 194421" src="https://user-images.githubusercontent.com/95010251/144348563-922842f8-7a47-439c-8eda-87294c7686c7.png">




>  * Case 2:

 curl -X 'POST'  'http://localhost:8000/store/' -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "store_name": "test_store"
}'
{"store_name":"test_store"}



<img width="971" alt="teststore" src="https://user-images.githubusercontent.com/95010251/144348652-04af740f-5e8e-4c51-9858-a34f92b06bf1.png">




Data in DB

<img width="922" alt="dbresponse" src="https://user-images.githubusercontent.com/95010251/144348595-37f44936-e076-43aa-bc7b-98d6ce9439f3.png">



## Room for Improvement:
- Can automate the whole process using Jenkins/GitLab pipeline.
- Modify README concisely.

## Contact:
- Developed by **Lohith Roy Peddenti**
- E-Mail: lohithroydevops@gmail.com
