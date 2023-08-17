#!/bin/bash
# This script displays all HTTP methods a server will accept.
curl -sI http://"$1" | awk '/Allow:/ {print $0}'
