from kafka import KafkaProducer
import time

bootstrap_servers = 'localhost:9092'
topic = 'churn'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

with open("WA_Fn-UseC_-Telco-Customer-Churn.csv", 'r') as file:
    for line in file:
        # Assuming each line in the CSV file is a separate message
        producer.send(topic, line.encode('utf-8'))
        time.sleep(15)

producer.close()
