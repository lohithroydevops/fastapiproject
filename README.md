
### Task Overview

This task is based on requirements provided to create containerized application with python uvicorn server and postgresql db as backend leveraging docker, docker-compose, and fastapi web framework for building api with python v.3.7.


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
  "store_name": "hhghjl"
}'

>  * Case 2:

 curl -X 'POST'  'http://localhost:8000/store/' -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
  "store_name": "test_store"
}'
{"store_name":"test_store"}


## Room for Improvement:
- Can automate the whole process using Jenkins/GitLab pipeline.
- Modify README concisely.

## Contact:
- Developed by **Lohith Roy Peddenti**
- E-Mail: lohithroydevops@gmail.com
