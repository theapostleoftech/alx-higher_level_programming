#!/bin/bash
# display all HTTP methods the server will accept using curl.
curl -s -X OPTIONS -I "$1" | grep "Allow:" | cut -d ' ' -f2-
