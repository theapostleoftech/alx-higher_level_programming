#!/bin/bash
# A bash script that takes in a URL and displays the size.
curl -s "$1" | wc -c
