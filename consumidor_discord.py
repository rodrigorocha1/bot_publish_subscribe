import pika
from pika.adapters.blocking_connection import BlockingChannel

from consumidor import Consumidor
from src.conexao_api.i_bikes_api import IBikesAPI


class ConsumidorDiscord(Consumidor):

    def __init__(self, api_bike: IBikesAPI):
        super().__init__(api_bike)

    def mostrar_mensagem(
            self,
            ch: BlockingChannel,
            method: pika.spec.Basic.Deliver,
            properties: pika.spec.BasicProperties, body: bytes
    ):
        pass



