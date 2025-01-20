# 3 discos: base, auxiliar e fim. começa no formato de torre e tem que chegar ao outro lado no formato de torre
def hanoi(n, origem, auxiliar, destino):
    if n == 1:
        print(f'Mova o disco 1 de {origem} para {destino}.')
        return 
    hanoi(n - 1, origem, auxiliar, destino)
    print(f'Mova o disco {n} de {origem} para {destino}.')
    hanoi(n - 1, auxiliar, destino, origem)

n = int(input('Digite o número de discos: '))
hanoi(n, 'A', 'C', 'B')