#!/bin/bash
# only status code
curl -so "$1" /dev/null -w '%{http_code}'
