# Modelo Biblioteca
# Classe LivroRenovavel

from src.model.livro import Livro
from src.model.exemplar import Exemplar

class LivroRenovavel(Livro):
    def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
        pass
