# Docker to Docker Connection
- Containerized a secured Sanic server.
- Developed a separate Dockerized application to interact with the Sanic server container.</br>
- Connected the two containers via a shared Docker network for seamless communication.
- This project demonstrates how to establish communication between two Docker containers using a shared Docker network. One container acts as a server (API or microservice), and the other as a client that makes requests to the server.

## Getting Started
- Make sure that you have [docker]([url](https://docs.docker.com/desktop/)) installed.
- After installing docker follow these steps to get the containers up and running: 
```shell
git clone https://github.com/AdityaUnal/docker-to-docker
cd time
docker network create time-network
docker compose -f time_docker/compose.yaml -f test/compose.yaml up -d
```
- Now you can access the entrypoint script using :
```shell
docker exec -it $(sudo docker ps -aq --filter ancestor=test-time-server) /bin/bash
``` 
