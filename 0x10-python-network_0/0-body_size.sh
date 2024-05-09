#!/bin/bash
#Bash script to display size of given url in bytes
curl -sI "$1" | grep -i "Content-Length" | cut " " -f 2
