#!/bin/bash
# This script POST http request.
curl -s "$1" -X POST -d email=test@gmail.com -d subject="I will always be here for PLD"
