#classe genero

from src.model.base import Base

class Genero(Base):
    def __init__(self, nome:str, identificacao: int = 0):
    # Chama o construtor da classe base com o parâmetro identificacao
        super().__init__(identificacao)
        # Atribui o nome ao atributo da instância
        self.nome = nome
