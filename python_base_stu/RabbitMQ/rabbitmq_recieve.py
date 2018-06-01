'''
Created on 2018年5月25日

@author: zhang
'''

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
                'localhost'))

channel = connection.channel()

channel.queue_declare(queue = 'hello',durable=True) #durable = Ture rabbitmq服务重启队列依然存在

def callback(ch,method,properties,body):
    print('[x] Received %r' % body)

    ch.basic_ack(delivery_tag=method.delivery_tag)
#可以根据消息处理快慢合理分配消息
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,

                      queue='hello2',

                      #no_ack = True)  #是否不需要回执，需要回执的话，没有回执，消息不会被消耗掉。
                      )
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
