#!/bin/bash
url=$1
response=$(curl -s -w "%{http_code}" -o >(cat - >&2) $url)
if [ "$response" == "200" ]; then
    curl -s $url
fi
