#!/bin/bash
# script to display available method on a url
curl -sIX OPTIONS $1 | grep -i allow | awk '{print $2}'
