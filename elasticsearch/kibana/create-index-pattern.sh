#!/usr/bin/env bash

url="http://localhost:5601"
index_pattern="packets-*"
time_field="timestamp"

# Create index pattern and get the created id
# curl -f to fail on error
curl -s -f -XPOST -H "Content-Type: application/json" -H "kbn-xsrf: anything" \
  "$url/api/saved_objects/index-pattern/$index_pattern" \
  -d"{\"attributes\":{\"title\":\"$index_pattern\",\"timeFieldName\":\"$time_field\"}}"

# Create the default index
curl -s -XPOST -H "Content-Type: application/json" -H "kbn-xsrf: anything" \
  "$url/api/kibana/settings/defaultIndex" \
  -d"{\"value\":\"$index_pattern\"}"