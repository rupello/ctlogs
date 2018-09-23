#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# download the filebeat container
docker pull docker.elastic.co/beats/filebeat:6.2.4

# uncomment the command below to setup dashboards
#docker run --net elasticsearch_elknet -i \
#        -v ${DIR}/filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml \
#        docker.elastic.co/beats/filebeat:6.2.4 setup --dashboards

# pass in -r <file> to specify a file or -i <interface>
certstream --json \
    | docker run --net elasticsearch_elknet -i \
        -v ${DIR}/filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml \
        docker.elastic.co/beats/filebeat:6.2.4