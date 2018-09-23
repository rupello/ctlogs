#!/usr/bin/env bash
echo "***"
echo "* executing elk-post-hooks"
echo "***"
curl -s -H "Content-Type: application/json" -XPOST \
    localhost:9200/_template/packets \
    --data-binary @/_config/mappings.json

echo "*** creating index pattern"
/_config/kibana/create-index-pattern.sh

echo "*** loading saved visualizations"
/_config/kibana/import-viz.sh

