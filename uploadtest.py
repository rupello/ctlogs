from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()

actions = [
  {
    "_index": "tickets-index",
    "_type": "tickets",
    "_id": j,
    "_source": {
        "any":"data" + str(j),
        "timestamp": datetime.utcnow()}
  }
  for j in range(0, 10)
]

helpers.bulk(es, actions)