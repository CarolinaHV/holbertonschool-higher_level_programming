#!/bin/bash
# only status code
curl -LI "$1" -o /dev/null -w '%{http_code}' -s
