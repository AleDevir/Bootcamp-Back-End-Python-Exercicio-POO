
from src.model.livro import Livro
from src.model.exemplar import Exemplar

class LivroRenovavel(Livro):
#Classe para livros que podem ter seu empréstimo renovado.
#Herda de Livro e adiciona a funcionalidade de renovação.

    def renovar_emprestimo_exemplar(self, exemplar: Exemplar) -> None:
#Renova o empréstimo do exemplar se as validações forem passadas.
#param exemplar: O exemplar que está sendo renovado.
#raises ValueError: Se o exemplar não pode ser renovado devido ao limite de renovações.

        if not exemplar.pode_renovar(self.renovacoes_permitidas):
            raise ValueError(f'Não é possível renovar o empréstimo do livro "{self.titulo}. Você já atingiu o limite máximo de renovações permitidas.')
        
        exemplar.acrescentar_numero_renovacoes()


    









