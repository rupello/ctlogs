### Example of Index Dump

```buildoutcfg
echo docker run --rm -ti --network=host -v `pwd`/indexdumps/apr15-panera/:/_dump taskrabbit/elasticsearch-dump \
--input=http://localhost:9200/packets-2018-04-15 \
--output=/_dump/packets-2018-04-15.data.json \
--type=data 

echo docker run --rm -ti --network=host -v `pwd`/indexdumps/apr15-panera/:/_dump taskrabbit/elasticsearch-dump \
--input=http://localhost:9200/packets-2018-04-15 \
--output=/_dump/packets-2018-04-15.mapping.json \
--type=mapping 
```