#!/bin/bash
# This script returns status code of an http request
curl -o /dev/null -s -w "%{http_code}" http://"$1" 
