#!/usr/bin/env bash

#res=$(curl -sI -X GET "$1")
res=$(curl -sX GET "$1" | grep "HTTP" | cut -d ' ' -f 2)
if [ "$res" == 301 ]; then
    echo "$res"
fi
