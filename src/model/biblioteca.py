'''
modelo Biblioteca
'''
from src.model.base import Base
from src.model.emprestimo import Emprestimo
from src.model.usuario import Usuario
from src.model.livro import Livro
from src.model.exemplar import Exemplar

class Biblioteca(Base):
    '''
    classe Biblioteca
    '''
    def __init__(
            self,
            usuarios: list[Usuario],
            livros: list[Livro],
            emprestimos: list[Emprestimo] = None,
            identificacao: int = 0,
        ) -> None:
        '''
        Inicialização
        '''
        super().__init__(identificacao)
        self._usuarios: list[Usuario] = usuarios
        self._livros: list[Livro] = livros
        self._emprestimos: list[Emprestimo] = []
        if emprestimos:
            self._emprestimos = emprestimos

    @property
    def usuarios(self) -> list[Usuario]:
        '''
        Lista de usuários        
        '''
        return self._usuarios

    @property
    def livros(self) -> list[Livro]:
        '''
        Lista de livros       
        '''
        return self._livros

    @property
    def emprestimos(self) -> list[Emprestimo]:
        '''
        Lista de empréstimos       
        '''
        return self._emprestimos

    def realizar_emprestimo(self, nome_usuario: str, titulo_livro: str) -> Emprestimo:
        '''
        Empresta ao usuario de nome o livro de título.
        Retorna o empréstimo.
        '''

    def devolver_emprestimo(
            self,
            identificacao_emprestimo: int
    ) -> Emprestimo:
        '''
        Devolve a biblioteca o exemplar do livro emprestado
        (informando a identificacao do empréstimo).
        Retorna o Emprestimo.
        '''

    def renovar_emprestimo(
            self,
            identificacao_emprestimo: int
    ) -> Emprestimo:
        '''
        Renova o emprestimo do livro (informando a identificacao do empréstimo) 
        Retorna o emprestimo renovado.
        '''
