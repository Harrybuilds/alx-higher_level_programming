#!/bin/bash
#using curl, display content of url if status == 200
#res=$(curl -sI -X GET "$1")
res=$(curl -sI "$1" | grep "HTTP" | cut -d ' ' -f 2)
if [ "$res" == 200 ]; then
    curl -sX GET "$1"
fi
