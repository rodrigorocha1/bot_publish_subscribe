from abc import ABC, abstractmethod
from typing import Dict


class IBots(ABC):

    @abstractmethod
    def enviar_mensagem(self, req: Dict):
        pass
