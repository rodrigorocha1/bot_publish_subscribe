from abc import ABC, abstractmethod
from typing import Dict


class IBikesAPI(ABC):

    @abstractmethod
    def consultar_dados_bicicleta(self, estacao: str) -> Dict:
        pass
