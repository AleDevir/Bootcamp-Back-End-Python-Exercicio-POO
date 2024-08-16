from datetime import datetime, timedelta
from typing import Final
from src.model.usuario import Usuario
from src.model.livro import Livro
from src.model.exemplar import Exemplar
from src.model.base import Base

EMPRESTADO: Final[str] = 'EMPRESTADO'
DEVOLVIDO: Final[str] = 'DEVOLVIDO'

class Emprestimo(Base):
    def __init__(
        self,
        usuario: Usuario,
        livro: Livro,
        exemplar: Exemplar,
        estado: str = EMPRESTADO,
        data_emprestimo: datetime = datetime.now(),
        data_devolucao: datetime | None = None,
        identificacao: int = 0
    ) -> None:
        super().__init__(identificacao)
        self.usuario: Usuario = usuario
        self.livro: Livro = livro
        self.exemplar: Exemplar = exemplar
        self.estado: str = estado
        self.data_emprestimo: datetime = data_emprestimo
        self.data_devolucao: datetime | None = data_devolucao

    def renovar(self) -> None:
        if self.estado == EMPRESTADO:
            self.livro.renovar_emprestimo_exemplar(self.exemplar)

    def devolver(self) -> None:
        if self.estado == EMPRESTADO:
            self.estado = DEVOLVIDO
            self.data_devolucao = datetime.now()
            self.livro.devolver_exemplar(self.exemplar.identificacao)
