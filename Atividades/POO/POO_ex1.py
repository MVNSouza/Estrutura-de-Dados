class Aluno:
    def __init__(self, nome, n1, n2):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self._media = (n1 + n2) / 2
    
    def passou(self):
        return self._media > 6
    
    def mais_um_ponto(self):
        self._media += 1




mateus = Aluno('mateus', 10, 2)
print(mateus.passou())
