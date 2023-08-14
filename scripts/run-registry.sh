#!/bin/bash

apt-get update && apt-get install -y nano curl

echo -e "\nConnector config:\n"
curl -X POST -H "Content-Type: application/json" -d @simplesink.json http://connect:8083/connectors -w "\n"

sleep 5
echo -e "\nConnector status:\n"
curl -X GET http://connect:8083/connectors/mongo-sink/status
