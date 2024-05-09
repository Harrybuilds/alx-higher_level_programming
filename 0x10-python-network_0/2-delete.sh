#!/bin/bash
# script that deletes a resource using curl
curl -sX DELETE "$1" | echo 
