#!/bin/bash
# This script displays the size of the body of the response.
curl -I "$1" | awk '/Content-Length:/ {print $2}'
