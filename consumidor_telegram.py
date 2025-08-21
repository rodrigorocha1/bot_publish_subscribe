from consumidor import Consumidor
from src.conexao_api.i_bikes_api import IBikesAPI
from src.conexao_api.bike_api import BikesApi
from src.mensageiro.ibots import IBots
from src.mensageiro.mensageiro_telegram import MensageiroTelegram


class ConsumidorTelegram(Consumidor):

    def __init__(self, api_bike: IBikesAPI, bot: IBots):
        super().__init__(api_bike, bot)
        self.__bot_telegram = MensageiroTelegram()


if __name__ == '__main__':
    ct = ConsumidorTelegram(api_bike=BikesApi(), bot=MensageiroTelegram())
    ct.executar()