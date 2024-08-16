'''
classe Usuario
'''

from src.model.base import Base

# Define a classe Usuario que herda da classe Base.
class Usuario(Base):
    def __init__(self, identificacao: int, nome: str, nacionalidade: str, telefone: str):
        # Chama o construtor da classe base (Base) para inicializar a identificação.
        super().__init__(identificacao)
        # Atributos específicos da classe Usuario.
        self.nome = nome  # Nome do usuário.
        self.nacionalidade = nacionalidade  # Nacionalidade do usuário.
        self.telefone = telefone  # Telefone do usuário.
        # Histórico de empréstimos do usuário, inicialmente uma lista vazia.
        self._historico_emprestimos = []

    # Método especial que retorna uma string representando o objeto Usuario.
    def __str__(self):
        # A string inclui o nome, nacionalidade, telefone e a quantidade de empréstimos no histórico.
        return f"Usuário: {self.nome}, Nacionalidade: {self.nacionalidade}, Telefone: {self.telefone}, Histórico de Empréstimos: {len(self._historico_emprestimos)} empréstimos"

    # Método para atualizar o telefone do usuário.
    def atualizar_telefone(self, novo_telefone: str):
        self.telefone = novo_telefone  # Atualiza o telefone do usuário.
        # Imprime uma mensagem confirmando a atualização.
        print(f"Telefone do usuário {self.nome} atualizado para {self.telefone}")

    # Método para adicionar um empréstimo ao histórico do usuário.
    def adicionar_emprestimo(self, emprestimo):
        self._historico_emprestimos.append(emprestimo)  # Adiciona o empréstimo ao histórico.
        # Imprime uma mensagem confirmando a adição.
        print(f"Empréstimo adicionado ao histórico do usuário {self.nome}.")

    # Método para remover um empréstimo do histórico do usuário.
    def remover_emprestimo(self, emprestimo):
        # Verifica se o empréstimo está no histórico.
        if emprestimo in self._historico_emprestimos:
            self._historico_emprestimos.remove(emprestimo)  # Remove o empréstimo do histórico.
            # Imprime uma mensagem confirmando a remoção.
            print(f"Empréstimo removido do histórico do usuário {self.nome}.")
        else:
            # Se o empréstimo não estiver no histórico, imprime uma mensagem informando que não foi encontrado.
            print(f"O empréstimo não foi encontrado no histórico do usuário {self.nome}.")

    # Propriedade para acessar o histórico de empréstimos do usuário.
    @property
    def historico_emprestimos(self):
        return self._historico_emprestimos  # Retorna a lista de empréstimos.
