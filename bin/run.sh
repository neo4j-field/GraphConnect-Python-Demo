#!/bin/bash


docker rmi $(docker images -a)

docker rm $(docker ps -a -f status=exited -q)

export IMAGE="graphconnect-bq-neo4j-client"

docker build -t $IMAGE .

docker run -d -p 7474:7474 $IMAGE
