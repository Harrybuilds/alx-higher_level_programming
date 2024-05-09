#!/bin/bash
#Bash script to display size of given url in bytes
curl -sI "$1" | grep "content-length" | cut " " -f 2
