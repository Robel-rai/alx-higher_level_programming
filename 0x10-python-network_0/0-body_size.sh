#!/bin/bash
# Get the byte size of the HTTP response header for a given URL
size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')
echo $size
