#!/bin/bash
# This script 
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
