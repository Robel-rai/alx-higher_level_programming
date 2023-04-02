#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
url=$1
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $url
