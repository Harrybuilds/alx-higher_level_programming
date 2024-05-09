#!/bin/bash
# script to get status code of a request with pipeline or redirect
curl -s -o /dev/null -w "%{http_code}" $1
