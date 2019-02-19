# k8s-rabbitmq-tut


## Part 1 - "Hello World" Set Up, send.py & receive.py
https://www.rabbitmq.com/tutorials/tutorial-one-python.html

Run RabbitMQ in docker container with manager dashboard on localhost:8080.  Default user:pass is guest:guest
```bash
docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management
```
* Docker Hub - https://hub.docker.com/_/rabbitmq

Instal the pika package.  Tutorial uses 0.11.0, I installed 0.13.0 and ran with no problems.
```bash
pip install pika
```

Python connection for RabbitMQ in docker container. **import pika** is required.
```python
connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@localhost:5672/%2F'))
```
* RabbitMQ Docs - https://pika.readthedocs.io/en/stable/examples/using_urlparameters.html

## Part 2 - Work Queues
https://www.rabbitmq.com/tutorials/tutorial-two-python.html

## Part 3 - Publish/Subscribe
A **binding** is a relationship between an exhange and a queue.

## Part 4 - Routing
Bindings can take an extra **routing_key** parameter. 

**Direct Exchange** - a message goes to the quesues whose **binding_key** exactly matches the **routing_key** of a message.


## Further Resources:
* RabbitMQ Production Checklist: https://www.rabbitmq.com/production-checklist.html
  