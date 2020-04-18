
import logging

logging.basicConfig(level=logging.DEBUG)

from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   bootstrap_servers=['localhost:9092'])

producer.send("test", b"test message")

producer.close()
