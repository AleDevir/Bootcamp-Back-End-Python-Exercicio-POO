'''
classe Autor
'''

from src.model.base import Base

class Autor(Base):

    def __init__(
            self,
            nome: str,
            identificacao: int = 0
    ) -> None:
        super().__init__(identificacao)
        self.nome: str = nome

    def __str__(self) -> str:
        return self.nome
