'''
classe LivroNaoRenovavel
'''

from abc import abstractmethod
from src.model.base import Base
from src.model.livro import Livro
from src.model.exemplar import Exemplar
from src.model.emprestimo import Emprestimo

class LivroNaoRenovavel(Livro):
    def __init__(self,
                identificacao: int, 
                titulo: str,
                exemplares: list[Exemplar],
                estado: str,
                renovacoes_permitidas: int):
        super().__init__(identificacao)
        self.titulo = titulo
        self.exemplares = exemplares
        self.renovacoes_permitidas = renovacoes_permitidas


    @property

    def possui_exemplar_disponivel(self) -> bool:
        pass

    def pode_ser_renovado(self, estado, renovacoes_permitidas) -> bool:
        if(estado != "Emprestado" and renovacoes_permitidas != 0):
            return True
        else:
            return False
            

    @abstractmethod
    
    def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
        pass
