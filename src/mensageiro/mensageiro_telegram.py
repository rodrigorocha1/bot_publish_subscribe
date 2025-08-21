import time
from typing import Dict, List
import re
import telebot
from src.config.config import Config
from src.formatador.formatador import Formatador


class MensageiroTelegram:
    def __init__(self):
        self.__TOKEN_TELEGRAM = Config.TOKEN_TELEGRAM
        self.__bot = telebot.TeleBot(self.__TOKEN_TELEGRAM)
        self.__CHAT_ID = Config.CHAT_ID

    def enviar_mensagem(self, req: Dict):
        estacoes: List = req['network']['stations']
        estacoes = sorted(estacoes, key=lambda x: int(x['name'].split('-')[0].strip()))

        for estacao in estacoes:
            latitude = estacao['latitude']
            longitude = estacao['longitude']
            map_link = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}&zoom=18"
            map_image_url = (
                f"https://staticmap.openstreetmap.de/staticmap.php?"
                f"center={latitude},{longitude}&zoom=15&size=400x200&markers={latitude},{longitude},red-pushpin"
            )
            titulo, descricao = Formatador.format_estacao(s=estacao, map_link=map_link)
            texto_completo = re.sub(
                r'([_\*\[\]\(\)~`>\#\+\-=|{}\.!])',
                r'\\\1', titulo
            ) + '\n' + re.sub(
                r'([_\*\[\]\(\)~`>\#\+\-=|{}\.!])',
                r'\\\1',
                descricao
            )
            self.__bot.send_message(self.__CHAT_ID, texto_completo, parse_mode="MarkdownV2")
            time.sleep(2)


if __name__ == '__main__':
    req = {
        "network": {
            "id": "bike-curitiba",
            "name": "BikeCuritiba",
            "location": {
                "latitude": -25.4299,
                "longitude": -49.2722,
                "city": "Curitiba",
                "country": "BR"
            },
            "href": "/v2/networks/bike-curitiba",
            "company": [
                "M1 Transportes Sustentáveis Ltda.",
                "M2 Soluções Em Engenharia Ltda.",
                "Tembici"
            ],
            "gbfs_href": "https://curitiba.publicbikesystem.net/customer/gbfs/v2/gbfs.json",
            "stations": [
                {
                    "id": "044005a83e2ebd69a2e93791d1555f89",
                    "name": "29 - Praça 29 de Março",
                    "latitude": -25.4287569006947,
                    "longitude": -49.2861399795242,
                    "timestamp": "2025-08-19T23:30:26.439219+00:00Z",
                    "free_bikes": 13,
                    "empty_slots": 6,
                    "extra": {
                        "uid": "1429",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646044,
                        "address": "Na rua de acesso a Praça 29 de Março, continuação Rua Desembargador Motta, Esquina com Rua Martim Afonso ",
                        "post_code": "80430-232",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 8,
                        "ebikes": 5,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "0d4d24964959860ebca3183aa8986b80",
                    "name": "10 - Shopping Itália",
                    "latitude": -25.43026985660947,
                    "longitude": -49.266516782075726,
                    "timestamp": "2025-08-19T23:30:26.438873+00:00Z",
                    "free_bikes": 14,
                    "empty_slots": 1,
                    "extra": {
                        "uid": "1410",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646131,
                        "address": "Rua Marechal Deodoro, 630",
                        "post_code": "80010-200",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 13,
                        "ebikes": 1,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "0fe1f7c41c0672d3d24333f1e66a50f5",
                    "name": "27 - Bigorrilho",
                    "latitude": -25.4321549949137,
                    "longitude": -49.2977599104387,
                    "timestamp": "2025-08-19T23:30:26.439181+00:00Z",
                    "free_bikes": 11,
                    "empty_slots": 4,
                    "extra": {
                        "uid": "1427",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646040,
                        "address": "Rua General Aristides Athayde Júnior, 657",
                        "post_code": "80730-370",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 11,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "14432c8700cb62396d1d9629913a28a9",
                    "name": "11 - Marechal Deodoro",
                    "latitude": -25.4292685609076,
                    "longitude": -49.2642711884978,
                    "timestamp": "2025-08-19T23:30:26.438892+00:00Z",
                    "free_bikes": 15,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1411",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646194,
                        "address": "R. Marechal Deodoro, 868 / Esquina com a Rua Tibagi",
                        "post_code": "80060-010",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 6,
                        "ebikes": 9,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "14b20dcd3f809291dfd78f91654371d9",
                    "name": "21 - João Turin",
                    "latitude": -25.445139002135065,
                    "longitude": -49.2824641139336,
                    "timestamp": "2025-08-19T23:30:26.439087+00:00Z",
                    "free_bikes": 3,
                    "empty_slots": 12,
                    "extra": {
                        "uid": "1421",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646195,
                        "address": "Travessa João Turin, 140",
                        "post_code": "80240-100",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 2,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "1bca0728c4a6c02ee252e359f689a289",
                    "name": "34 - Cândido de Abreu",
                    "latitude": -25.4201136905753,
                    "longitude": -49.2693199785828,
                    "timestamp": "2025-08-19T23:30:26.439278+00:00Z",
                    "free_bikes": 19,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1434",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646056,
                        "address": "Av. Cândido de Abreu, 469",
                        "post_code": "80530-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 4,
                        "ebikes": 15,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "1ed663f717b93a5c596e23803b25afc8",
                    "name": "04 - Praça Rui Barbosa",
                    "latitude": -25.435931,
                    "longitude": -49.2717515,
                    "timestamp": "2025-08-19T23:30:26.438737+00:00Z",
                    "free_bikes": 19,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1404",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646199,
                        "address": "R. André de Barros, 16",
                        "post_code": "80010-110",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 3,
                        "ebikes": 16,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "220f86e07c81deeb32669310041f202c",
                    "name": "42 - Terminal Portão",
                    "latitude": -25.476884536910468,
                    "longitude": -49.292607969540505,
                    "timestamp": "2025-08-19T23:30:26.439432+00:00Z",
                    "free_bikes": 21,
                    "empty_slots": 2,
                    "extra": {
                        "uid": "1442",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646100,
                        "address": "Av. República Argentina, 3492",
                        "post_code": "80215-270",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 23,
                        "normal_bikes": 0,
                        "ebikes": 21,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "26b102a0069a69c3c41f48e7e3f976d5",
                    "name": "05 - Praça Zacarias",
                    "latitude": -25.432517,
                    "longitude": -49.272226,
                    "timestamp": "2025-08-19T23:30:26.438768+00:00Z",
                    "free_bikes": 16,
                    "empty_slots": 3,
                    "extra": {
                        "uid": "1405",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646167,
                        "address": "Al. Dr. Muricy, 533",
                        "post_code": "80020-060",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 1,
                        "ebikes": 15,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "36bdb983de97068afb6a745dd236d3d6",
                    "name": "09 - Hard Rock",
                    "latitude": -25.4380092285766,
                    "longitude": -49.2814294291538,
                    "timestamp": "2025-08-19T23:30:26.438853+00:00Z",
                    "free_bikes": 10,
                    "empty_slots": 5,
                    "extra": {
                        "uid": "1409",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646200,
                        "address": "R. Comendador Araújo, 692",
                        "post_code": "80420-063",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 9,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "3b61c0049ab1207a1e38e9f5f976aa26",
                    "name": "31 - Largo da Ordem ",
                    "latitude": -25.4280427,
                    "longitude": -49.2741431,
                    "timestamp": "2025-08-19T23:30:26.439696+00:00Z",
                    "free_bikes": 4,
                    "empty_slots": 11,
                    "extra": {
                        "uid": "1471",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646209,
                        "address": "Al. Dr. Muricy, 1011",
                        "post_code": "80020-040",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 2,
                        "ebikes": 2,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "46ed511454f2d8b9a30a84b8bf20b935",
                    "name": "08 - Vicente Machado",
                    "latitude": -25.4354715406325,
                    "longitude": -49.2826324005316,
                    "timestamp": "2025-08-19T23:30:26.438834+00:00Z",
                    "free_bikes": 11,
                    "empty_slots": 8,
                    "extra": {
                        "uid": "1408",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646128,
                        "address": "Rua Vicente Machado, 632 / Esquina com R. Desembargador Mota",
                        "post_code": "80420-010",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 5,
                        "ebikes": 6,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "4c256df8640eaf64c64199fccd115af5",
                    "name": "15 - Mercado Municipal",
                    "latitude": -25.4343826579185,
                    "longitude": -49.2575412329964,
                    "timestamp": "2025-08-19T23:30:26.438971+00:00Z",
                    "free_bikes": 12,
                    "empty_slots": 7,
                    "extra": {
                        "uid": "1415",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646086,
                        "address": "Av. Sete de Setembro, oposto ao 1882 / Na calçada em frente a entrada do Mercado Municipal",
                        "post_code": "80060-150",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 5,
                        "ebikes": 7,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "585082a181b85859e4a78605dfcaa585",
                    "name": "28 - Agrárias",
                    "latitude": -25.410055,
                    "longitude": -49.2487254,
                    "timestamp": "2025-08-19T23:30:26.439199+00:00Z",
                    "free_bikes": 15,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1428",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646055,
                        "address": "Rua dos funcionários, 1416",
                        "post_code": "82590-300",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 15,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "62539422817728913af35170c5a5d62e",
                    "name": "50 - Igreja do Portão",
                    "latitude": -25.473397,
                    "longitude": -49.294535,
                    "timestamp": "2025-08-19T23:30:26.439602+00:00Z",
                    "free_bikes": 17,
                    "empty_slots": 2,
                    "extra": {
                        "uid": "1450",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646039,
                        "address": "R. Carlos Dietzsch, 44 ",
                        "post_code": "80330-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 3,
                        "ebikes": 14,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "64f0ac76e982793c61feffb62086b695",
                    "name": "02 - Sesc Paço da Liberdade",
                    "latitude": -25.4300616794306,
                    "longitude": -49.2692833096877,
                    "timestamp": "2025-08-19T23:30:26.439640+00:00Z",
                    "free_bikes": 14,
                    "empty_slots": 5,
                    "extra": {
                        "uid": "1459",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646050,
                        "address": "R. Riachuelo, 38",
                        "post_code": "80020-250",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 5,
                        "ebikes": 9,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "65d9040519e719589fb64218d63f6ba2",
                    "name": "01 - Estácio ",
                    "latitude": -25.431704786518836,
                    "longitude": -49.24121592908326,
                    "timestamp": "2025-08-19T23:30:26.439678+00:00Z",
                    "free_bikes": 3,
                    "empty_slots": 8,
                    "extra": {
                        "uid": "1470",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646122,
                        "address": "Avenida Senador Souza Naves, 1715",
                        "post_code": "80050-152",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 11,
                        "normal_bikes": 0,
                        "ebikes": 3,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "66501168862ace482067e12595eae5fa",
                    "name": "26 - Prudente de Moraes",
                    "latitude": -25.429883,
                    "longitude": -49.28258,
                    "timestamp": "2025-08-19T23:30:26.439161+00:00Z",
                    "free_bikes": 11,
                    "empty_slots": 4,
                    "extra": {
                        "uid": "1426",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646165,
                        "address": "Rua Prof. Fernando Moreira x Al. Prudente de Moraes",
                        "post_code": "80730-330",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 5,
                        "ebikes": 6,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "66a74cc460a0a17a19454fec81c89e10",
                    "name": "35 - Prefeitura",
                    "latitude": -25.4183944,
                    "longitude": -49.2684711,
                    "timestamp": "2025-08-19T23:30:26.439297+00:00Z",
                    "free_bikes": 7,
                    "empty_slots": 12,
                    "extra": {
                        "uid": "1435",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646151,
                        "address": "Av. Cândido de Abreu, 660 /próximo ao Tubo",
                        "post_code": "80530-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 2,
                        "ebikes": 5,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "6d74066f0c86c8eb23baa968513db6e3",
                    "name": "23 - Parque Barigui II",
                    "latitude": -25.432391429856644,
                    "longitude": -49.31295959595973,
                    "timestamp": "2025-08-19T23:30:26.439124+00:00Z",
                    "free_bikes": 17,
                    "empty_slots": 2,
                    "extra": {
                        "uid": "1423",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646161,
                        "address": "R. Gal Mario Tourinho, altura no n° 2489 / No canteiro central, após os semáforo.",
                        "post_code": "80740-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 7,
                        "ebikes": 10,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "7ad2e4f41e3c421c28fc251eb330eb6a",
                    "name": "41 - Estação Rodoferroviária",
                    "latitude": -25.4359306634073,
                    "longitude": -49.2569163546697,
                    "timestamp": "2025-08-19T23:30:26.439413+00:00Z",
                    "free_bikes": 10,
                    "empty_slots": 5,
                    "extra": {
                        "uid": "1441",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646183,
                        "address": "Av. Presidente Affonso Camargo, 534 , altura da Rua Gen. Carneiro/ Na calçada de acesso a Rodoviária",
                        "post_code": "80060-090",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 2,
                        "ebikes": 8,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "84672d51c89045dcba0f250a6036ab55",
                    "name": "12 - Reitoria",
                    "latitude": -25.4273300330418,
                    "longitude": -49.2622678465011,
                    "timestamp": "2025-08-19T23:30:26.438911+00:00Z",
                    "free_bikes": 20,
                    "empty_slots": 3,
                    "extra": {
                        "uid": "1412",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646064,
                        "address": "R. Dr. Faivre, 420 ",
                        "post_code": "80060-140",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 23,
                        "normal_bikes": 13,
                        "ebikes": 7,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "85add9ea9b714a484e8a28407f51f9cb",
                    "name": "40 - Terminal Cabral",
                    "latitude": -25.406915,
                    "longitude": -49.253414,
                    "timestamp": "2025-08-19T23:30:26.439394+00:00Z",
                    "free_bikes": 16,
                    "empty_slots": 3,
                    "extra": {
                        "uid": "1440",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646184,
                        "address": "R. Luciano Cardinale, 01 / esquina com Rua Chichorro Júnior / na grama",
                        "post_code": "80035-130",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 1,
                        "ebikes": 15,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "879227004ef015db2187dcb4a7e258c9",
                    "name": "03 - Praça Carlos Gomes",
                    "latitude": -25.433286879797084,
                    "longitude": -49.27086124596873,
                    "timestamp": "2025-08-19T23:30:26.439658+00:00Z",
                    "free_bikes": 7,
                    "empty_slots": 8,
                    "extra": {
                        "uid": "1460",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646036,
                        "address": "Av. Mal. Floriano Peixoto, 306",
                        "post_code": "80010-150",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 7,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "8f84895b68f289387b444af27edbddd0",
                    "name": "43 - Praça do Japão",
                    "latitude": -25.446086,
                    "longitude": -49.288941,
                    "timestamp": "2025-08-19T23:30:26.439451+00:00Z",
                    "free_bikes": 6,
                    "empty_slots": 13,
                    "extra": {
                        "uid": "1443",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646143,
                        "address": "Av. Sete de Setembro, 5300 ",
                        "post_code": "80240-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 0,
                        "ebikes": 6,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "91e4c9347e29229cc923f3ea9710dc4d",
                    "name": "18 - 24 de Maio",
                    "latitude": -25.4402443506638,
                    "longitude": -49.2728285182166,
                    "timestamp": "2025-08-19T23:30:26.439030+00:00Z",
                    "free_bikes": 12,
                    "empty_slots": 3,
                    "extra": {
                        "uid": "1418",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646184,
                        "address": "Rua 24 de Maio, 399",
                        "post_code": "80220-060",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 4,
                        "ebikes": 8,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "99d8a19a18a4e686151e537d91ca0501",
                    "name": "51 - Praça Tiradentes",
                    "latitude": -25.429435,
                    "longitude": -49.2707969,
                    "timestamp": "2025-08-19T23:30:26.439621+00:00Z",
                    "free_bikes": 13,
                    "empty_slots": 6,
                    "extra": {
                        "uid": "1458",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646201,
                        "address": "Travessa Tobias de Macedo, 16",
                        "post_code": "80020-210",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 3,
                        "ebikes": 10,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "9e3aa4cc070e57d84767cf4df98089d3",
                    "name": "22 - Parque Barigui I",
                    "latitude": -25.423181,
                    "longitude": -49.305544,
                    "timestamp": "2025-08-19T23:30:26.439105+00:00Z",
                    "free_bikes": 16,
                    "empty_slots": 7,
                    "extra": {
                        "uid": "1422",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646183,
                        "address": "Rua Doutor Aluízio França, 465, esquina com Av. Candido Hartmann / no estacionamento",
                        "post_code": "82010-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 23,
                        "normal_bikes": 14,
                        "ebikes": 2,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "9e5dbaf6beaf6c0896a809fa97b5c67e",
                    "name": "14 - SENAC Centro",
                    "latitude": -25.4336581627,
                    "longitude": -49.2660327715488,
                    "timestamp": "2025-08-19T23:30:26.438951+00:00Z",
                    "free_bikes": 19,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1414",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646212,
                        "address": "R. André de Barros, 715",
                        "post_code": "80010-080",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 19,
                        "ebikes": 0,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "a12d05d54a8b3e41d7a527efa00de207",
                    "name": "30 - Praça da Espanha",
                    "latitude": -25.4358,
                    "longitude": -49.28686,
                    "timestamp": "2025-08-19T23:30:26.439239+00:00Z",
                    "free_bikes": 12,
                    "empty_slots": 7,
                    "extra": {
                        "uid": "1430",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646111,
                        "address": "Alameda Dr. Carlos de Carvalho, 1263",
                        "post_code": "80420-170",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 0,
                        "ebikes": 12,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "a17fd5dd58188ffcbc055b5c691bcbac",
                    "name": "07 - Visconde do Rio Branco",
                    "latitude": -25.434986507067,
                    "longitude": -49.2783048417248,
                    "timestamp": "2025-08-19T23:30:26.438813+00:00Z",
                    "free_bikes": 10,
                    "empty_slots": 4,
                    "extra": {
                        "uid": "1407",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646036,
                        "address": "Rua Visconde do Rio Branco, oposto ao 1541 / esquina com Rua Com. Araújo",
                        "post_code": "80420-210",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 2,
                        "ebikes": 8,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "a27f3add8cd302964e907ddb01cb6b35",
                    "name": "16 - Largo Baden Powel",
                    "latitude": -25.4356160674615,
                    "longitude": -49.2615691242899,
                    "timestamp": "2025-08-19T23:30:26.438991+00:00Z",
                    "free_bikes": 9,
                    "empty_slots": 6,
                    "extra": {
                        "uid": "1416",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646054,
                        "address": "Av. Sete de Setembro, 2346 ",
                        "post_code": "80230-085",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 8,
                        "ebikes": 1,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "a59e46f1f459dbe06831ac4e335e46f9",
                    "name": "24 - Terminal Campina do Siqueira",
                    "latitude": -25.4365307267069,
                    "longitude": -49.3085810188107,
                    "timestamp": "2025-08-19T23:30:26.439143+00:00Z",
                    "free_bikes": 23,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1424",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646040,
                        "address": "R. Padre Anchieta, 3037",
                        "post_code": "80740-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 23,
                        "normal_bikes": 11,
                        "ebikes": 12,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "b70480d3414edf909111aece80a048a7",
                    "name": "32 - Praça Dezenove de Dezembro",
                    "latitude": -25.4255989,
                    "longitude": -49.270218,
                    "timestamp": "2025-08-19T23:30:26.439716+00:00Z",
                    "free_bikes": 16,
                    "empty_slots": 3,
                    "extra": {
                        "uid": "1472",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646064,
                        "address": "R. Barão do Serro Azul, 384",
                        "post_code": "80020-180",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 7,
                        "ebikes": 9,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "bbe06fde17a1b746a7582f5168e0cd4c",
                    "name": "13 - Mariano Torres",
                    "latitude": -25.4303627499146,
                    "longitude": -49.2625094577514,
                    "timestamp": "2025-08-19T23:30:26.438932+00:00Z",
                    "free_bikes": 13,
                    "empty_slots": 2,
                    "extra": {
                        "uid": "1413",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646161,
                        "address": "R. Mariano Torres, 451",
                        "post_code": "80060-120",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 5,
                        "ebikes": 8,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "bcdb8c41b804b501d8f70615fec11fbd",
                    "name": "38 - Constantino Marochi",
                    "latitude": -25.4158335857949,
                    "longitude": -49.2609290695051,
                    "timestamp": "2025-08-19T23:30:26.439357+00:00Z",
                    "free_bikes": 5,
                    "empty_slots": 10,
                    "extra": {
                        "uid": "1438",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646094,
                        "address": "R. Constantino Marochi, 570 / Esquina com Av. João Gualberto",
                        "post_code": "80030-360",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 5,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "c186fe84db4609902cbfb7c7582dabab",
                    "name": "20 - Rua Buenos Aires",
                    "latitude": -25.4420037481837,
                    "longitude": -49.2787757120821,
                    "timestamp": "2025-08-19T23:30:26.439068+00:00Z",
                    "free_bikes": 11,
                    "empty_slots": 4,
                    "extra": {
                        "uid": "1420",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646044,
                        "address": "R. Buenos Aires, 499 ",
                        "post_code": "80250-070",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 10,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "c37a276e60935b5c55ced0ae396e29a2",
                    "name": "48 - Shopping Água Verde",
                    "latitude": -25.463174,
                    "longitude": -49.29036,
                    "timestamp": "2025-08-19T23:30:26.439564+00:00Z",
                    "free_bikes": 6,
                    "empty_slots": 9,
                    "extra": {
                        "uid": "1448",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646057,
                        "address": "R. Matogrosso, 45 / Esquina com Av. República Argentina",
                        "post_code": "80320-120",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 2,
                        "ebikes": 4,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "c97752099e4e11293af812363fa43f0f",
                    "name": "25 - Gastão Câmara.",
                    "latitude": -25.4387041,
                    "longitude": -49.3012064,
                    "timestamp": "2025-08-19T23:30:26.439736+00:00Z",
                    "free_bikes": 5,
                    "empty_slots": 14,
                    "extra": {
                        "uid": "1476",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646193,
                        "address": "25 - Gastão Câmara.",
                        "post_code": "80730-290",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 1,
                        "ebikes": 4,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "da5d95f6894cd1fcd4e4c7cd9383422f",
                    "name": "17 - Câmara Municipal",
                    "latitude": -25.4381016,
                    "longitude": -49.2683528,
                    "timestamp": "2025-08-19T23:30:26.439010+00:00Z",
                    "free_bikes": 15,
                    "empty_slots": 0,
                    "extra": {
                        "uid": "1417",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646103,
                        "address": "Av. Mal. Floriano Peixoto 885",
                        "post_code": "82590-300",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 9,
                        "ebikes": 6,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "db2c905a7afb1f18f776c3e5c862452c",
                    "name": "37 - Parque São Lourenço",
                    "latitude": -25.3872007116733,
                    "longitude": -49.2674180914774,
                    "timestamp": "2025-08-19T23:30:26.439337+00:00Z",
                    "free_bikes": 10,
                    "empty_slots": 13,
                    "extra": {
                        "uid": "1437",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646191,
                        "address": "R. Mateus Leme 4715",
                        "post_code": "82200-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 23,
                        "normal_bikes": 1,
                        "ebikes": 9,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "dc08ed1ce40e79cdc02076c067077883",
                    "name": "46 - Água Verde",
                    "latitude": -25.45387,
                    "longitude": -49.288187,
                    "timestamp": "2025-08-19T23:30:26.439509+00:00Z",
                    "free_bikes": 1,
                    "empty_slots": 14,
                    "extra": {
                        "uid": "1446",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646168,
                        "address": "Av. Água Verde, oposto ao 1728. Esquina com Av. Rep. Argentina",
                        "post_code": "80620-010",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 0,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "e489c7979b1fb5910d92daca340949c2",
                    "name": "47 - República Argentina",
                    "latitude": -25.4588188393534,
                    "longitude": -49.288715012442,
                    "timestamp": "2025-08-19T23:30:26.439527+00:00Z",
                    "free_bikes": 4,
                    "empty_slots": 7,
                    "extra": {
                        "uid": "1447",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646129,
                        "address": "R. Murilo do Amaral Ferreira, 51 / Esquina com República Argentina",
                        "post_code": "80620-120",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 11,
                        "normal_bikes": 0,
                        "ebikes": 4,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "eb912d1cf5eb1eed66c45d7289a8cd43",
                    "name": "49 - Pedro Macedo",
                    "latitude": -25.468244,
                    "longitude": -49.295373,
                    "timestamp": "2025-08-19T23:30:26.439584+00:00Z",
                    "free_bikes": 6,
                    "empty_slots": 9,
                    "extra": {
                        "uid": "1449",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646190,
                        "address": "R. Sylvio Zeny, 134 / próximo ao Colégio Estadual Pedro Macedo",
                        "post_code": "80610-310",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 6,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f0b563da903626f442e7499e6bad30ed",
                    "name": "36 - Museu Oscar Niemeyer",
                    "latitude": -25.410411916633,
                    "longitude": -49.2659739477465,
                    "timestamp": "2025-08-19T23:30:26.439317+00:00Z",
                    "free_bikes": 17,
                    "empty_slots": 2,
                    "extra": {
                        "uid": "1436",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646122,
                        "address": "R. Mal. Hermes, 946 ",
                        "post_code": "80530-230",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 7,
                        "ebikes": 10,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f11614bbb9f2424c3049bb6831ee624a",
                    "name": "19 - Praça Oswaldo Cruz",
                    "latitude": -25.4397862971417,
                    "longitude": -49.2757265576647,
                    "timestamp": "2025-08-19T23:30:26.439049+00:00Z",
                    "free_bikes": 14,
                    "empty_slots": 1,
                    "extra": {
                        "uid": "1419",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646044,
                        "address": "R. Lamenha Lins, 354",
                        "post_code": "80250-020",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 13,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f21bc293eda48f4e223142496dfd1283",
                    "name": "45 - Getúlio Vargas",
                    "latitude": -25.4513337490637,
                    "longitude": -49.2886812060878,
                    "timestamp": "2025-08-19T23:30:26.439489+00:00Z",
                    "free_bikes": 4,
                    "empty_slots": 11,
                    "extra": {
                        "uid": "1445",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646160,
                        "address": "Av. Pres. Getúlio Vargas, 3084 / Esquina com Av. Rep. da Argentina",
                        "post_code": "80240-040",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 1,
                        "ebikes": 3,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f5770a13c52238dedc117351a70445c6",
                    "name": "33 - Passeio Público",
                    "latitude": -25.4237562137314,
                    "longitude": -49.2680743935643,
                    "timestamp": "2025-08-19T23:30:26.439257+00:00Z",
                    "free_bikes": 14,
                    "empty_slots": 1,
                    "extra": {
                        "uid": "1433",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646078,
                        "address": "Av. João Gualberto na lateral do Passeio Público",
                        "post_code": "80030-000",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 6,
                        "ebikes": 8,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f8b31144d529668722912fdb90aaf83d",
                    "name": "44 - Pátio Batel",
                    "latitude": -25.4440046624908,
                    "longitude": -49.2903675481214,
                    "timestamp": "2025-08-19T23:30:26.439470+00:00Z",
                    "free_bikes": 4,
                    "empty_slots": 11,
                    "extra": {
                        "uid": "1444",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646151,
                        "address": "Rua Bruno Figueira 601",
                        "post_code": "80440-220",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 4,
                        "ebikes": 0,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "f9ba9fcef2f21a5a2484acb8feb01abd",
                    "name": "06 - Praça Osório",
                    "latitude": -25.433183902343,
                    "longitude": -49.2768283453299,
                    "timestamp": "2025-08-19T23:30:26.438791+00:00Z",
                    "free_bikes": 13,
                    "empty_slots": 6,
                    "extra": {
                        "uid": "1406",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646087,
                        "address": "Praça Gen. Osório, 333",
                        "post_code": "80020-010",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 19,
                        "normal_bikes": 3,
                        "ebikes": 10,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                },
                {
                    "id": "fce3b871d99e235a304e83df9081efe9",
                    "name": "39 - Moysés Marcondes",
                    "latitude": -25.412688,
                    "longitude": -49.258581,
                    "timestamp": "2025-08-19T23:30:26.439375+00:00Z",
                    "free_bikes": 5,
                    "empty_slots": 10,
                    "extra": {
                        "uid": "1439",
                        "renting": True,
                        "returning": True,
                        "last_updated": 1755646087,
                        "address": "Rua Moyses Marcondes, 505",
                        "post_code": "80030-001",
                        "payment": [
                            "key",
                            "transitcard",
                            "creditcard",
                            "phone"
                        ],
                        "payment-terminal": True,
                        "altitude": 0.0,
                        "slots": 15,
                        "normal_bikes": 0,
                        "ebikes": 5,
                        "has_ebikes": True,
                        "rental_uris": {},
                        "virtual": False
                    }
                }
            ]
        }
    }

    mt = MensageiroTelegram()
    mt.enviar_mensagem(req=req)
