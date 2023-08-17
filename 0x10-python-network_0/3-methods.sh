#!/bin/bash
# This script displays all HTTP methods a server will accept.
curl -sI "$1" | awk '/Allow:/ {print $2, $3, $4}'
