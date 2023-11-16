class Cromossomo:
    def __init__(self, valor, estado_final):
        self.valor = valor
        self.aptidao = self.calcular_aptidao(estado_final)
        self.porcentagem_aptidao = 0

    def calcular_aptidao(self, estado_final):
        nota = 0
        for i in range(len(estado_final)):
            if self.valor.__contains__(estado_final[i]):
                nota += 5
            if self.valor[i] == estado_final[i]:
                nota += 50
        return nota

    def __lt__(self, other):
        return self.aptidao > other.aptidao

    def __eq__(self, other):
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False