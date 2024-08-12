'''
classe Usuario
'''
class Usuario(Base):
    def __init__(self, identificacao: int, nome: str, nacionalidade: str, telefone: str):
        super().__init__(identificacao)
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.telefone = telefone

    def __str__(self):
        return f"Usuário: {self.nome}, Nacionalidade: {self.nacionalidade}, Telefone: {self.telefone}"

    def atualizar_telefone(self, novo_telefone: str):
        self.telefone = novo_telefone
        print(f"Telefone do usuário {self.nome} atualizado para {self.telefone}")
