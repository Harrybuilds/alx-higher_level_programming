#!/bin/bash
# script to display available method on a url
curl -sI $1 | grep -i allow | awk '{print $2}'
