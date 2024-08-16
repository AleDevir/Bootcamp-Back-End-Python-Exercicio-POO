'''
Classe Base
'''

from abc import ABC

# Define a classe Base como uma classe abstrata que herda de ABC (Abstract Base Class).
class Base(ABC):
    def __init__(self, identificacao: int = 0) -> None:
        super().__init__()  # Chama o construtor da superclasse ABC.
        # Atributo protegido (não estritamente privado, mas indicado como de uso interno) que armazena a identificação do objeto.
        self._identificacao: int = identificacao

    @property
    def identificacao(self) -> int:
        # Propriedade que retorna o valor do atributo _identificacao.
        return self._identificacao

    def __eq__(self, other: object) -> bool:
        # Método especial que permite comparar dois objetos da classe Base (ou derivadas) usando o operador de igualdade (==).
        # Se o outro objeto não for uma instância de Base, retorna NotImplemented, indicando que a comparação não é válida.
        if not isinstance(other, Base):
            return NotImplemented
        # Se o outro objeto é uma instância de Base, compara as identificações dos dois objetos.
        return self._identificacao == other._identificacao

    def __hash__(self) -> int:
        # Método especial que permite que objetos da classe Base sejam usados em estruturas de dados que requerem hashing, como conjuntos (set) e dicionários (dict).
        # O hash é calculado com base no valor de _identificacao, garantindo que objetos com a mesma identificação tenham o mesmo hash.
        return hash(self._identificacao)

    def __str__(self) -> str:
        # Método especial que define a representação em string do objeto, usada, por exemplo, quando o objeto é impresso com print().
        # Retorna uma string que mostra o nome da classe e a identificação do objeto.
        return f'{self.__class__.__name__}(ID: {self._identificacao})'
