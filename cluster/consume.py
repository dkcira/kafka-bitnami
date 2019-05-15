from kafka import KafkaConsumer
consumer = KafkaConsumer('mytopic')
for msg in consumer:
    print(msg)
