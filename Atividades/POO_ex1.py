class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self._media = (n1 + n2) / 2




mateus = Aluno('mateus', 10, 2)
