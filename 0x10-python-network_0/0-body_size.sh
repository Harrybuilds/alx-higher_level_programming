#!/bin/bash
#Bash script to display size of given url in bytes
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
