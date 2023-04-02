#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
url=$1
curl -sI -X OPTIONS $url | grep -i Allow | awk '{print $2}'
