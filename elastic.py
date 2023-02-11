import csv
from datetime import datetime
import re
from elasticsearch import Elasticsearch


# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Index the information dictionary into Elasticsearch


list_of_data = []

with open('test.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    data_list = list(reader)
    keys = data_list[0]
    default_value = 'None'
    for line in data_list[1:]:
        values = str(*line)

        replacements = [
            ('"', ''), 
            ('://?', 'None'), 
            ('0000-00-00 00:00:00', '0001-01-01 00:00:00'),
            ('0000-00-00\n', '0001-01-01 00:00:00')
        ]

        for search, replace in replacements:
            values = values.replace(search, replace)

        values = values.split(',')
        data = dict(zip(keys, values))
        data = {key: data.get(key, default_value) for key in keys}
        list_of_data.append(data)



for index, doc in enumerate(list_of_data):
    res = es.index(index='my-index', id=index, body=doc)
    print(res['result'])


es.indices.refresh(index="my-index")
print(es.cat.count(index="my-index", format="json"))