#!/bin/bash
# cURL a JSON file
curl -sH "Content-Type: application/json" --data "$(cat "$2")" "$1"
