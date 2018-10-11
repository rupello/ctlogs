import argparse
import json
import logging
import sys
import queue
import threading

from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

from signal import signal, SIGPIPE, SIG_DFL

import certstream

parser = argparse.ArgumentParser(description='Connect to the CertStream and process CTL list updates.')

parser.add_argument('--verbose', action='store_true', default=False, dest='verbose', help='Display debug logging.')
parser.add_argument('--url', default="wss://certstream.calidog.io", dest='url', help='Connect to a certstream server.')


def uploader(queue):
    es = Elasticsearch()
    id = 0
    while True:
        actions = []
        for i in range(100):
            actions.append(
                {
                    "_index": "certstream-test",
                    "_type": "_doc",
                    "_id": id,
                    "_source": {
                        "message": queue.get(),
                        "timestamp": datetime.utcnow()}
                }
            )
            id+=1
        print(helpers.bulk(es, actions))


def main():
    args = parser.parse_args()

    # Ignore broken pipes
    signal(SIGPIPE, SIG_DFL)

    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

    logging.basicConfig(format='[%(levelname)s:%(name)s] %(asctime)s - %(message)s', level=log_level)

    q = queue.Queue()
    t = threading.Thread(target=uploader,args=(q,))
    t.start()

    def _handle_messages(message, context):
        q.put(message, block=False);
        #sys.stdout.flush()
        #sys.stdout.write(json.dumps(message) + "\n")
        #sys.stdout.flush()

    certstream.listen_for_events(_handle_messages, args.url, skip_heartbeats=True)

if __name__ == "__main__":
    main()
