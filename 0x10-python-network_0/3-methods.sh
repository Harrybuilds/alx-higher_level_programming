#!/bin/bash
# script to display available method on a url

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -X OPTIONS -i "$1"
