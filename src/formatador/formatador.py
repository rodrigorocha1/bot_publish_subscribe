from datetime import datetime
from typing import Dict, Tuple


class Formatador:
    @staticmethod
    def format_estacao(s: Dict, map_link: str) -> Tuple[str, str]:
        titulo = f"🚲 Estação {s['name']}"
        description = (
            f"📍 **Endereço:** {s['extra'].get('address', 'N/A')}\n\n"
            f"🚴 **Bikes livres:** {s.get('free_bikes', 0)}\n\n"
            f"🚲 **Total normal:** {s['extra'].get('normal_bikes', 0)}\n\n"
            f"⚡ **Total bikes elétricas:** {s['extra'].get('ebikes', 0)}\n\n"
            f"💳 **Formas de pagamento:** {', '.join(s['extra'].get('payment', []))}\n\n"
            f"🕒 **Data de atualização da estação:** "
            f"{datetime.fromtimestamp(s['extra'].get('last_updated', 0)).strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            f"🌐 [Abrir mapa]({map_link})"
        )
        return titulo, description
