
project deployed on remote server:
http://78.27.236.114:8006/

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
