#!/bin/bash

# where the application config dir should be mounted
export CONFIG_DIR=$1

#docker run -p host:exposed my-image
docker run -t -d --name smoochbot -v ${CONFIG_DIR}:/mnt/config -p 5000:5000 claytantor/smoochbot4py:latest
