#!/bin/bash

export IMAGE="graphconnect-bq-neo4j-client"
export NEO4J_IMAGE_VERSION="latest"
export GCP_BASE_REPOSITORY="graphconnect-bq-neo4j-client"
export GCP_BASE_IMAGE=$IMAGE
export GCP_PUSH_STRING="us-east1-docker.pkg.dev/neo4j-se-team-201905/${GCP_BASE_REPOSITORY}/${GCP_BASE_IMAGE}"


docker build -t "${IMAGE}" .

docker tag "${IMAGE} \
${GCP_PUSH_STRING}/${GCP_BASE_IMAGE}:${NEO4J_IMAGE_VERSION}"



docker push "${GCP_PUSH_STRING}"