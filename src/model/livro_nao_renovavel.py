'''
classe LivroNaoRenovavel
'''
from src.model.livro import Livro
from src.model.exemplar import Exemplar

class LivroNaoRenovavel(Livro):
   def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
      raise ValueError(f"Este livro não pode ser renovado.")
