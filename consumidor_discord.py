from src.conexao_api.bike_api import BikesApi
from consumidor import Consumidor
from src.conexao_api.i_bikes_api import IBikesAPI
from src.mensageiro.ibots import IBots
from src.mensageiro.mensageiro_discord import MensageiroDiscord


class ConsumidorDiscord(Consumidor):

    def __init__(self, api_bike: IBikesAPI, bot: IBots):
        super().__init__(api_bike=api_bike, bot=bot)
        self.bot = MensageiroDiscord()


if __name__ == "__main__":
    cd = ConsumidorDiscord(api_bike=BikesApi(), bot=MensageiroDiscord())
    cd.executar()
