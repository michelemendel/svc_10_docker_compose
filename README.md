# DevOps 10 - Docker Compose

- https://github.com/YakirBar/sv-college-docker-compose/blob/main/EX%20-%20Docker%20Compose.md

1. Create SQL Database MySQL Using Docker Compose
2. Create Python Web Application
3. Create Connection To MySQL Using Environment Variable + Volume
4. Create New Dockerfile
5. Build Your Image Using Tag python_mysql:v0.1
6. Test Locally The Application VIA Docker Compose (Using Port 3000)
7. Uplaod Your Docker Compose File To Git

## Commands used

```bash
docker build -t python_mysql:v0.1 .

docker-compose up -d --build

docker volume ls

curl localhost:3000

docker-compose down
```
