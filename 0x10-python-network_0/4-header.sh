#!/usr/bin/env bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL provided as argument
url="$1"

# Send GET request with header
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display response body
echo "$response"
