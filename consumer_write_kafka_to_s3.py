from confluent_kafka import Consumer, KafkaException
import json
from smart_open import open

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Add your IP here
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'test-topic'
consumer.subscribe([topic])

try:
    count = 0
    while True:
        # Poll for new messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            # Handle any potential error
            if msg.error().code() == "404":
                # End of partition event
                print(f'Reached end of partition {msg.partition()}')
            else:
                # Error occurred
                raise KafkaException(msg.error())

        # Decode the message value
        value = msg.value().decode('utf-8')

        # Write the message value to S3
        with open(f"s3://my-data-bucket-aa-s3/kafka_msgs/test_topic_msg_{count}.data", 'w') as file:
            file.write(value)

        count += 1

except KeyboardInterrupt:
    # Close the consumer on keyboard interrupt
    consumer.close()
