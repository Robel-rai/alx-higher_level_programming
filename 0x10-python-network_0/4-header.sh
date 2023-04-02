#!/bin/bash
# Send a GET request to a given URL with a header variable.
url=$1
curl -s -H "X-School-User-Id: 98" $url
