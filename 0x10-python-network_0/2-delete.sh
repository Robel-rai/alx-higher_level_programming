#!/bin/bash
# Send a DELETE request to a given URL and display the response body.
url=$1
curl -s -X DELETE $url
