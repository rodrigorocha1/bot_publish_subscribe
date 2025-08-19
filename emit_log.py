#!/usr/bin/env python
import pika
import sys
import time

credenciais = pika.PlainCredentials('rodrigo', '123456')

parametros_conexao = pika.ConnectionParameters(
    host='172.30.0.10',
    port=5672,
    virtual_host='/',
    credentials=credenciais
)

connection = pika.BlockingConnection(parametros_conexao)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

while True:
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(f" [x] Sent {message}")
    time.sleep(2)  # espera 2 segundos antes de enviar a próxima mensagem
