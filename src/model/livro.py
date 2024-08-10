'''
Classe Livro
'''
import livro_renovavel
import livro_nao_renovavel
import genero
import autor
import base
import exemplar
from abc import ABC, abstractmethod

class Livro(base):
    def __init__(self, identificacao: int,titulo: str, editora: str, generos: list[genero.Genero], exemplares: list[exemplar.Exemplar], autores: list[autor.Autor], renovacoes_permitidas: int):
        super().__init__(identificacao)
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares = exemplares
        self.autores = autores
        self.renovacoes_permitidas = renovacoes_permitidas

    @property
    def possui_exemplar_disponivel(self) -> bool:
        pass

    def retirar_exemplar(self) -> exemplar.Exemplar:
        pass

    def pode_ser_renovado(self) -> bool:
        pass
    
    @abstractmethod
    def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
        pass

    def devolver_exemplar(self, identificacao_exemplar) -> None:
        pass