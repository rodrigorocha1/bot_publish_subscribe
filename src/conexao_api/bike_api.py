from typing import Dict
from src.config.config import Config
import requests
from src.conexao_api.i_bikes_api import IBikesAPI


class BikesApi(IBikesAPI):

    def __init__(self):
        self.__url = Config.URL_API

    def consultar_dados_bicicleta(self, estacao: str) -> Dict:
        url = f'{self.__url}{estacao}'
        req = requests.get(url=url)
        req = req.json()
        return req
