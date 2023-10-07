# Thư viện pika cần được install thông qua lệnh pip3 install pika

import pika

CLOUDAMQP_URL = 'amqp://admin:admin@localhost:56720'

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
params = pika.URLParameters(CLOUDAMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='demo')  # Declare a queue

def callback(ch, method, properties, body):
    print(" [x] Received " + str(body))


channel.basic_consume('demo',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()