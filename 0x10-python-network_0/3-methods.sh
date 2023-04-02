#!/bin/bash
url=$1
curl -sI -X OPTIONS $url | grep -i Allow | awk '{print $2}'
