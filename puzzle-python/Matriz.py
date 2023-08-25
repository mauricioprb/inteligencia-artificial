import random

class Matriz:
    def __init__(self, dimensao):
        self.matriz = [[0] * dimensao for _ in range(dimensao)]
        self.dimensao = dimensao
        self.linha = 0
        self.coluna = 0
        self.direcoes = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1)
        }

    def embaralhar(self):
        numeros = list(range(self.dimensao * self.dimensao))
        random.shuffle(numeros)
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                self.matriz[i][j] = numeros.pop()
                if self.matriz[i][j] == 0:
                    self.linha = i
                    self.coluna = j

    def exibir(self):
        for linha in self.matriz:
            print(" ".join(map(str, linha)))
        print(f"POSICAO 0 = {self.linha}{self.coluna}")

    def mover(self, direcao):
        dl, dc = self.direcoes[direcao]
        nova_linha, nova_coluna = self.linha + dl, self.coluna + dc

        if 0 <= nova_linha < self.dimensao and 0 <= nova_coluna < self.dimensao:
            self.matriz[self.linha][self.coluna], self.matriz[nova_linha][nova_coluna] = \
                self.matriz[nova_linha][nova_coluna], self.matriz[self.linha][self.coluna]
            self.linha, self.coluna = nova_linha, nova_coluna
