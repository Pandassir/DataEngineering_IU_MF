'''The Supermarket Data Source'''

import json
import os
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer

fruits = ["apple", "pears", "bananas"]
regions = ["germany", "switzerland"]
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)

KAFKA_BROKER = 'localhost:29092'  
KAFKA_TOPIC = 'supermarket'  

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    key_serializer=str.encode,  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)

for i in range(1100000):
    key = "fruits"  

    data = {
        "fruit": random.choice(fruits),
        "region": random.choice(regions),
        "quantity": random.randint(1, 20),
        "timestamp": (start_date + (random.random() * (end_date - start_date))).isoformat()
    }

    future = producer.send(KAFKA_TOPIC, key=key, value=data)

    try:
        future.get(timeout=10)  
        print(f"Nachricht {i} erfolgreich gesendet.")
    except Exception as e:
        print(f"Beim Senden der Nachricht {i} ist ein Fehler aufgetreten: {e}")


producer.flush()







