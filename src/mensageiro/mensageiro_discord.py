import time
from typing import Dict, List
from discord_webhook import DiscordEmbed, DiscordWebhook
from src.formatador.formatador import Formatador

from src.config.config import Config


class MensageiroDiscord:

    def __init__(self):
        self.__webhook = DiscordWebhook(
            url=Config.URL_DISCORD,
            username='BotSistema'
        )

    def enviar_mensagem(self, req: Dict):
        estacoes: List = req['network']['stations']
        estacoes = sorted(estacoes, key=lambda x: int(x['name'].split('-')[0].strip()))

        batch_size = 9
        for i in range(0, len(estacoes), batch_size):
            batch = estacoes[i:i + batch_size]

            for s in batch:
                latitude = s['latitude']
                longitude = s['longitude']
                map_link = f"https://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}&zoom=18"
                map_image_url = (
                    f"https://staticmap.openstreetmap.de/staticmap.php?"
                    f"center={latitude},{longitude}&zoom=15&size=400x200&markers={latitude},{longitude},red-pushpin"
                )
                titulo, descricao = Formatador.format_estacao(s=s, map_link=map_link)
                embed = DiscordEmbed(
                    title=f'{titulo}\n',
                    description=descricao,
                    color="03b2f8"
                )
                embed.set_image(url=map_image_url)
                embed.set_footer(text="Atualizado automaticamente")
                embed.set_timestamp()
                self.__webhook.add_embed(embed)

            response = self.__webhook.execute()
            print(response.status_code, response.json())
            self.__webhook.remove_embeds()
            time.sleep(1)