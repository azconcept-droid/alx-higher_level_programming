#!/bin/bash
# This script displays all HTTP methods a server will accept.
curl -isLX OPTIONS "$1" | awk '/OPTIONS/ {print $2, $3, $4}'
