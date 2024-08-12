'''
Classe Emprestimo
'''

from datetime import datetime, timedelta
from typing import Final
from src.model.usuario import Usuario
from src.model.livro import Livro
from src.model.exemplar import Exemplar
from src.model.base import Base


EMPRESTADO: Final[str] = 'EMPRESTADO'
DEVOLVIDO: Final[str] = 'DEVOLVIDO'

class Emprestimo (Base):
    '''
    classe Emprestimo
    '''
    def __init__ (
            self,
            usuario:Usuario,
            livro:Livro,
            exemplar:Exemplar,
            estado: str = EMPRESTADO,
            data_emprestimo: datetime = datetime.now(), 
            data_devolucao: datetime | None = None,
            identificacao: int = 0
        ) -> None:
        '''
        Inicialização
        '''
        super().__init__(identificacao)
        self._usuario: Usuario = usuario
        self._livro: Livro = livro
        self._exemplar: Exemplar = exemplar
        self._estado: str = estado
        self._data_emprestimo: datetime = data_emprestimo
        self._data_devolucao: datetime | None = data_devolucao

    def renovar(self) -> None:
        '''
        Renovar       
        '''

    def devolver(self) -> None:
        '''
        Devolver     
        '''
