#!/bin/bash
#script to post json data inside a file to given url
curl -s -X POST -H "Content-Type: application/json" -d "@$2" $1
