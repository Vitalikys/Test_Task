## The Challenge Test Task
Build an online service for generating CSV files with fake (dummy) data using Python and Django:
* Any user can log in to the system with a username and password. You can use generic views provided by Django to implement these features. Registering new users via the admin interface is enough. Note, that you do not need to implement a user profile interface to support password change or similar functionality.
* Any logged-in user can create any number of data schemas to create datasets with fake data.
* Each such data schema has a name and a list of columns with names and specified data types.

### All Task Description see file: "PLANEKS Test task.pdf" 
#### project is deployed here:
http://78.27.236.114:8006/

### Credentials for testing:
username: admin  
password: admin

start in docker:
```shell
docker compose up -d --build 
```

open bash in running container:
```shell
docker exec -it app_csv_generator  bash
```

start Tests:
```shell
./manage.py test
```
