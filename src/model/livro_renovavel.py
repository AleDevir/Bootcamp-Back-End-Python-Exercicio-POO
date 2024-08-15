class LivroRenovavel(Livro):

    def __init__(self, renovacoes_permitidas: int, identificacao: int,titulo: str, editora: str, generos: list[genero.Genero], exemplares: list[exemplar.Exemplar], autores: list[autor.Autor]):
        super().__init__(identificacao)
        self.renovacoes_permitidas = renovacoes_permitidas
        self.titulo = titulo
        self.autores = autores

    def renovacoes(self):
        if self.renovacoes_permitidas > 0:
            self.renovacoes_permitidas -= 1
            print(f"Renovação realizada. Renovações disponíveis: {self.renovacoes_permitidas}")
        else:
            print("Número máximo de renovações atingido.")

    def restabelecer_renovacoes(self):
        self.renovacoes_permitidas = self.renovacoes_permitidas
        print(f"Renovações restabelecidas. Renovações disponíveis: {self.renovacoes_permitidas}")

    def __str__(self):
        return f"{self.titulo} por {self.autores} - Renovações permitidas: {self.renovacoes_permitidas}"


    









