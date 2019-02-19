import pika
import time

# set the connection
# connecting to kubernetes hosted HA cluster
connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:5672/%2F'))
channel = connection.channel()

# Create the hello queue, which is where the message is delivered
channel.queue_declare(queue='hello')

# use the empty exhange field to use the special exchange
# special exhcange - passes message to queue matching routing key
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# gently close
connection.close()