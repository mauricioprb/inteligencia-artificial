from Matriz import Matriz

if __name__ == "__main__":
    dimensao = int(input("Digite a Dimensão da matriz: "))
    matriz = Matriz(dimensao)
    matriz.embaralhar()
    matriz.exibir()

    while True:
        movimento = input("Digite o movimento (cima/baixo/esquerda/direita/sair): ").lower()
        if movimento == "sair":
            break
        elif movimento in matriz.direcoes:
            matriz.mover(movimento)
            matriz.exibir()
        else:
            print("Movimento inválido!")
