#!/bin/bash
# This script that returns status code
curl -o /dev/null -s -w "%{html_code}" http://"$1" 
