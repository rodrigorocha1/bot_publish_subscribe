import pika
from pika.adapters.blocking_connection import BlockingChannel

from consumidor import Consumidor
from src.conexao_api.i_bikes_api import IBikesAPI


class ConsumidorTelegram(Consumidor):

    def __init__(self, api_bike: IBikesAPI):
        super().__init__(api_bike)

    def mostrar_mensagem(
            self,
            ch: BlockingChannel,
            method: pika.spec.Basic.Deliver,
            properties: pika.spec.BasicProperties, body: bytes
    ):
        pass

    def executar(self):
        canal = self._conexao.channel()
        canal, nome_fila = self.configurar_fila(canal=canal)
        canal.basic_consume(
            queue=nome_fila,
            on_message_callback=self.mostrar_mensagem,
            auto_ack=True

        )
        canal.start_consuming()
