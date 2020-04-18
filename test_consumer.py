
import logging

#logging.basicConfig(level=logging.DEBUG)

from kafka import KafkaConsumer
from json import dumps

consumer = KafkaConsumer("test",
   bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print(msg)

consumer.close()
