
# Sử dụng thư viện pika để xử lý RabbitMQ message với giao thức AMQP trong Python ...
# Tham khảo code tại đây:
# https://www.lhsang.dev/posts/technique/rabbitmq/
# using CloudAMQP (https://www.cloudamqp.com/)
from datetime import datetime

# Thư viện pika cần được install thông qua lệnh pip3 install pika
import pika

CLOUDAMQP_URL = 'amqp://admin:admin@localhost:56720'

# establish a connection with RabbitMQ server.
params = pika.URLParameters(CLOUDAMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# create queue with name 'demo'
channel.queue_declare(queue='demo')
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Ready to send a message

strTime = str(datetime.now())
channel.basic_publish(exchange='logs',
                      routing_key='key1',
                      body='Hello world from tdchien! Current time: ' + strTime)

print(" >> Sent message at time: " + strTime)

# close connection
connection.close()
