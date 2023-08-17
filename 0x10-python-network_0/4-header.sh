#!/bin/bash
# This script sends a GET request & displays the body of the response
curl -s -H "X-School-User-Id: 98" http://"$1"
