import pika

# set the connection
# connecting to kubernetes hosted HA cluster
connection = pika.BlockingConnection(pika.ConnectionParameters('https://rabbitmq:5672'))
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