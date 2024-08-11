
# Gerenciamento de Biblioteca
# Livro Renovavel


from src.model.base import Base
from src.model.emprestimo import Emprestimo
from src.model.usuario import Usuario
from src.model.livro import Livro
from src.model.exemplar import Exemplar

class LivroRenovavel(Livro):

    def __init__(renovacoes_permitidas):
        self.renovacoes_permitidas = renovacoes_permitidas

