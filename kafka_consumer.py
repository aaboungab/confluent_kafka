from confluent_kafka import Consumer
from confluent_kafka.admin import TopicMetadata
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

try:
    conf = {'bootstrap.servers': 'localhost:9092',
            'group.id': 'mygroup'}
    consumer = Consumer(conf)
    topic = "test-topic"
    consumer.subscribe([topic])
    consumer.poll(1.0)
    # print(dir(consumer.poll(5.0)))
    # print(dir(consumer.subscribe))
    # print(consumer.subscribe([topic]))
    # print(consumer.subscribe([topic]))
    # consumer.subscribe(["test-topic"])
    
except BaseException as e:
    print(f"Error occurred: {e}")

## METADATA list of attributes
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# 'brokers', 'cluster_id', 'controller_id', 'orig_broker_id', 'orig_broker_name', 'topics']

