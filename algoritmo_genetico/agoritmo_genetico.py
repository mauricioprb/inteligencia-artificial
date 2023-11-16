import random
from cromossomo import Cromossomo
from util import Util

class AlgoritmoGenetico:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for _ in range(tamanho_populacao):
            populacao.append(Cromossomo(Util.gerar_palavra(len(estado_final)), estado_final))

    @staticmethod
    def ordenar(populacao):
        populacao.sort(reverse=True)

    @staticmethod
    def exibir(populacao):
        for cromossomo in populacao:
            print(f"Cromossomo: {cromossomo.valor} - {cromossomo.aptidao} - {cromossomo.porcentagem_aptidao}")

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        if not populacao:
            return 

        nova_populacao.append(populacao[0])

        qtd_selecionados = int(taxa_selecao * len(populacao) / 100)
        i = 1
        while i <= qtd_selecionados:
            c1 = random.choice(populacao)
            c2 = random.choice(populacao)
            c3 = random.choice(populacao)

            torneio = sorted([c1, c2, c3], key=lambda x: x.aptidao, reverse=True)
            selecionado = torneio[0]

            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1

    @staticmethod
    def selecionar_por_roleta(populacao, nova_populacao, taxa_selecao):
        aptidao_total = sum(c.aptidao for c in populacao)

        for c in populacao:
            c.porcentagem_aptidao = c.aptidao * 100 / aptidao_total
            if c.porcentagem_aptidao == 0:
                c.porcentagem_aptidao = 1

        sorteio = [c for c in populacao for _ in range(int(c.porcentagem_aptidao))]

        qtd_selecionados = int(taxa_selecao * len(populacao) / 100)
        nova_populacao.append(populacao[0])

        for _ in range(qtd_selecionados):
            selecionado = random.choice(sorteio)
            nova_populacao.append(selecionado)
            sorteio.remove(selecionado)

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        i = 0
        qtd_reproduzidos = int(taxa_reproducao * len(populacao) / 100)

        while i < qtd_reproduzidos:
            pai = random.choice(populacao)
            mae = random.choice(populacao)

            s_pai = pai.valor
            s_mae = mae.valor

            s_filho1 = s_pai[:len(s_pai)//2] + s_mae[len(s_mae)//2:]
            s_filho2 = s_mae[:len(s_mae)//2] + s_pai[len(s_pai)//2:]

            nova_populacao.extend([
                Cromossomo(s_filho1, estado_final),
                Cromossomo(s_filho2, estado_final)
            ])
            i += 2

        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()

    @staticmethod
    def mutar(populacao, estado_final):
        qtd_mutantes = random.randint(0, len(populacao) // 5)

        for _ in range(qtd_mutantes):
            mutante = random.choice(populacao)
            valor_mutado = list(mutante.valor)

            caracter_mutante = random.choice(mutante.valor)
            caracter_sorteado = random.choice(Util.letras)
            valor_mutado[mutante.valor.index(caracter_mutante)] = caracter_sorteado

            mutante.valor = ''.join(valor_mutado)
            mutante.calcular_aptidao(estado_final)

        return populacao

    @staticmethod
    def main():
        tamanho_populacao = int(input("Tamanho da população: "))
        estado_final = input("Palavra desejada: ")
        taxa_selecao = int(input("Taxa de seleção (entre 20 a 40%): "))
        taxa_reproducao = 100 - taxa_selecao
        taxa_mutacao = int(input("Taxa de mutação (entre 5 a 10%): "))
        qtd_geracoes = int(input("Quantidade de gerações: "))

        populacao = []
        nova_populacao = []

        AlgoritmoGenetico.gerar_populacao(populacao, tamanho_populacao, estado_final)
        AlgoritmoGenetico.ordenar(populacao)
        print("\nGeração 1")
        AlgoritmoGenetico.exibir(populacao)

        for i in range(1, qtd_geracoes):
            AlgoritmoGenetico.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
            AlgoritmoGenetico.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)
            if taxa_mutacao != 0 and len(populacao) != 0 and i % (len(populacao) // taxa_mutacao) == 0:
                nova_populacao = AlgoritmoGenetico.mutar(nova_populacao, estado_final)
            populacao.clear()
            populacao.extend(nova_populacao)
            nova_populacao.clear()
            AlgoritmoGenetico.ordenar(populacao)
            print(f"\n\nGeração {i + 1}")
            AlgoritmoGenetico.exibir(populacao)

if __name__ == "__main__":
    AlgoritmoGenetico.main()