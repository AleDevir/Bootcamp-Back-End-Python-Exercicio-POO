'''
Classe Base
'''

from abc import ABC
class Base(ABC):
    def __init__(self, identificacao: int = 0) -> None:
        super().__init__()
        self._identificacao: int = identificacao

    @property
    def identificacao(self) -> int:
        return self._identificacao
