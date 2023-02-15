# test-elasticsearch

## Run Project

For running elasticsearch:
```sh
docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.6.1
```

After that need deploy data to elasticsearch using script:

```sh
python elastic.py
```

And then we run Vue app:

```sh
npm run serve
```
