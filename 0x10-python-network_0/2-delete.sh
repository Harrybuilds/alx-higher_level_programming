#!/bin/bash
# script that deletes a resource using curl
# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request and capture response
response=$(curl -sX DELETE "$1")

# Display response body
echo "$response"
