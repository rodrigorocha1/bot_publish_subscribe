from typing import Tuple
import pika
from pika.adapters.blocking_connection import BlockingChannel
from src.config.config import Config
from src.conexao_api.i_bikes_api import IBikesAPI
from src.conexao_api.bike_api import BikesApi
from abc import ABC, abstractmethod


class Consumidor(ABC):

    def __init__(self, api_bike: IBikesAPI):
        self._credenciais = pika.PlainCredentials(
            Config.USR_RABBITMQ,
            Config.PWD_RABBITMQ
        )
        self._parametros_conexao = pika.ConnectionParameters(
            host=Config.HOST_RABBITMQ,
            port=Config.PORTA_RABBITMQ,
            virtual_host='/',
            credentials=self._credenciais
        )
        self._conexao = pika.BlockingConnection(parameters=self._parametros_conexao)
        self._api_bike = api_bike

    @abstractmethod
    def mostrar_mensagem(
            self,
            ch: BlockingChannel,
            method: pika.spec.Basic.Deliver,
            properties: pika.spec.BasicProperties,
            body: bytes
    ):
        # print('=' * 20)
        # print(body)
        # print('=' * 20)
        pass

    def configurar_fila(self, canal: BlockingChannel) -> Tuple[BlockingChannel, str]:
        canal.exchange_declare(
            exchange='bicicleta_curitiba',
            exchange_type='fanout'
        )
        result = canal.queue_declare(queue='', exclusive=True)
        nome_fila = result.method.queue
        canal.queue_bind(exchange='bicicleta_curitiba', queue=nome_fila)
        return canal, nome_fila

    def executar(self):
        canal = self._conexao.channel()
        canal, nome_fila = self.configurar_fila(canal=canal)
        canal.basic_consume(
            queue=nome_fila,
            on_message_callback=self.mostrar_mensagem,
            auto_ack=True

        )
        canal.start_consuming()
