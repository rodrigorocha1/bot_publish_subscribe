import time
import pika
from src.config.config import Config
from src.conexao_api.i_bikes_api import IBikesAPI
from src.conexao_api.bike_api import BikesApi
import json


class Produtor:

    def __init__(self, api_bike: IBikesAPI):
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

    def rodar(self):
        canal = self.__conexao.channel()
        canal.exchange_declare(
            exchange='bicicleta_curitiba',
            exchange_type='fanout'
        )
        while True:
            try:

                message = self.__api_bike.consultar_dados_bicicleta(estacao='bike-curitiba')

                canal.basic_publish(
                    exchange='bicicleta_curitiba',
                    routing_key='',
                    body=json.dumps(message)
                )

                time.sleep(0.5 * 60)

            except KeyboardInterrupt:
                print('Fechado')
                self.__conexao.close()


if __name__ == "__main__":
    p = Produtor(
        api_bike=BikesApi()
    )
    p.rodar()
