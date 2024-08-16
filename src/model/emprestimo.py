from datetime import datetime, timedelta
from typing import Final, Optional
from src.model.usuario import Usuario
from src.model.livro import Livro
from src.model.exemplar import Exemplar
from src.model.base import Base

EMPRESTADO: Final[str] = 'EMPRESTADO'
DEVOLVIDO: Final[str] = 'DEVOLVIDO'

class Emprestimo(Base):
    '''
    classe Emprestimo
    '''
    def __init__(
            self,
            usuario: Usuario,
            livro: Livro,
            exemplar: Exemplar,
            estado: str = EMPRESTADO,
            data_emprestimo: datetime = datetime.now(), 
            data_devolucao: Optional[datetime] = None,
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
        self._data_devolucao: Optional[datetime] = data_devolucao

    def renovar(self) -> None:
        '''
        Renovar
        '''
        if hasattr(self._livro, 'max_renovacoes'):
            if self._livro.max_renovacoes > 0:
                self._livro.max_renovacoes -= 1
                self._data_emprestimo += timedelta(days=30)  # Exemplo de renovação por mais 30 dias
            else:
                print("Número máximo de renovações atingido.")
        else:
            self._data_emprestimo += timedelta(days=30)  # Exemplo de renovação por mais 30 dias

    def devolver(self) -> None:
        '''
        Devolver
        '''
        self._estado = DEVOLVIDO
        self._data_devolucao = datetime.now()
        self._livro.adicionar_exemplar(self._exemplar)

    def __str__(self) -> str:
        return (f"Empréstimo[ID: {self._identificacao}, Usuário: {self._usuario.nome}, "
                f"Livro: {self._livro.titulo}, Exemplar: {self._exemplar.identificacao}, "
                f"Estado: {self._estado}, Data de Empréstimo: {self._data_emprestimo}, "
                f"Data de Devolução: {self._data_devolucao}]")
