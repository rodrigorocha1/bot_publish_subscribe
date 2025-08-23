import json
from typing import Tuple, Dict, List
import pika # t
from pika.adapters.blocking_connection import BlockingChannel

from src.mensageiro.ibots import IBots
from src.mensageiro.mensageiro_discord import MensageiroDiscord
from src.config.config import Config
from src.conexao_api.i_bikes_api import IBikesAPI
from src.conexao_api.bike_api import BikesApi


from src.mensageiro.mensageiro_telegram import MensageiroTelegram


class Consumidor:

    def __init__(self, api_bike: IBikesAPI, bots_mensageiro: List[IBots]):
        self.__credenciais = pika.PlainCredentials(
            Config.USR_RABBITMQ,
            Config.PWD_RABBITMQ
        )
        self.__parametros_conexao = pika.ConnectionParameters(
            host=Config.HOST_RABBITMQ,
            port=Config.PORTA_RABBITMQ,
            virtual_host='/',
            credentials=self.__credenciais
        )
        self.__conexao = pika.BlockingConnection(parameters=self.__parametros_conexao)
        self.__api_bike = api_bike
        self.__bots = bots_mensageiro

    def enviar_mensagem(self, req: Dict):
        for bot in self.__bots:
            bot.enviar_mensagem(req=req)

    def mostrar_mensagem(
            self,
            ch: BlockingChannel,
            method: pika.spec.Basic.Deliver,
            properties: pika.spec.BasicProperties,
            body: bytes
    ):
        req = json.loads(body.decode())

        self.enviar_mensagem(req=req)

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
        canal = self.__conexao.channel()
        canal, nome_fila = self.configurar_fila(canal=canal)
        canal.basic_consume(
            queue=nome_fila,
            on_message_callback=self.mostrar_mensagem,
            auto_ack=True

        )
        canal.start_consuming()


if __name__ == '__main__':
    c = Consumidor(api_bike=BikesApi(), bots_mensageiro=[
            MensageiroDiscord(),
            MensageiroTelegram()
        ])
    c.executar()
