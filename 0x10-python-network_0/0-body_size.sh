#!/bin/bash
# This script displays the size of the body of the response.
curl -s "$1" -X GET -d Content-Length
