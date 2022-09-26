#!/bin/bash
# This script that returns status code
curl -o /dev/null -s -w "%{http_code}" http://"$1" 
