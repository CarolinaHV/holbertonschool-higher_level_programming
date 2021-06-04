#!/bin/bash
# cURL a JSON file
curl -s -H "Content-Type: application/json" "$1" -d @$2
