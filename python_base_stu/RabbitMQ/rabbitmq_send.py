'''
Created on 2018年5月25日

@author: zhang
'''

import pika
#创建链接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
#创建通道
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello',durable=True)#durable = Ture rabbitmq服务重启队列依然存在

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello9999 World!',
                      # properties 会将消息持久化，没被消耗掉的消息重启服务依然存在，前提队列存在
                      properties = pika.BasicProperties(
                          delivery_mode = 2
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()