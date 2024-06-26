"""This file contain rabbitmq producer"""
import pika
from schemas import schema

class RabbitMQ:
    """This class will publish message and close connection"""
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.exchange_name = 'subscription_updates'
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')

    def publish_message(self, subscription_update: schema.Subscription):
        email = subscription_update.email
        is_active = subscription_update.is_active
        self.channel.basic_publish(exchange=self.exchange_name, routing_key=email, body={'email': email, 'is_active': is_active})
    
    def close_connection(self):
        if self.connection.is_open:
            self.connection.close()
