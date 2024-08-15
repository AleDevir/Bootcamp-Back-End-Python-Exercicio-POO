'''
Classe Livro
'''
from src.model.genero import Genero
from src.model.autor import Autor
from src.model.base import Base
from src.model.exemplar import Exemplar
from abc import abstractmethod

class Livro(Base):
    def __init__(self, identificacao: int,titulo: str, editora: str, generos: list[Genero], exemplares: list[.Exemplar], autores: list[Autor], renovacoes_permitidas: int):
        super().__init__(identificacao)
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares = exemplares
        self.autores = autores
        self.renovacoes_permitidas = renovacoes_permitidas

    @property
    def possui_exemplar_disponivel(self) -> bool:
        return any(volume.disponivel for volume in self.exemplares)

    def retirar_exemplar(self) -> exemplar.Exemplar:
        for volume in self.exemplares:
            if volume.disponivel:
                volume.disponivel = False
                return volume
        raise Exception("Nenhum exemplar disponível.")

    def pode_ser_renovado(self) -> bool:
        return self.renovacoes_permitidas > 0
    
    @abstractmethod
    def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
        pass

    def devolver_exemplar(self, identificacao_exemplar) -> None:
        for volume in self.exemplares:
            if volume.identificacao == identificacao_exemplar:
                volume.disponivel = True
                return volume
        raise Exception("Exemplar não encontrado.")
