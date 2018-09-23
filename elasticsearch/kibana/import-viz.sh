#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
find ${DIR}/viz -name '*.json' | xargs -L 1 python3 ${DIR}/kibana-importer.py --json