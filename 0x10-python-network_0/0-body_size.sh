#!/bin/bash
#Bash script to display size of given url in bytes

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body
#size=$(curl -s -w "%{size_download}" -o /dev/null "$1")
curl -sI "$1" | grep "content-length" | cut " " -f 2
echo "$size"

