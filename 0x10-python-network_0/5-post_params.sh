#!/usr/bin/env bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./$0 <URL>"
    exit 1
fi

# URL provided as argument
url="$1"

# Send GET request with header
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"

# Display response body
echo "$response"
