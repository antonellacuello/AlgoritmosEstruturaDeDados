# Calcule uma seq. de passos que resolva o problema da Torre de Hanoi (passar todos os discos de um pino A para outro C, utilizando um pino auxiliar
#  B, cada disco pode ficar apenas em cima de discos maiores).

def torreDeHanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f'Mova o disco de {origem} para {destino}.')
    else:
        # Passo 1: Mover n - 1 discos para o auxiliar
        torreDeHanoi(n - 1, origem, auxiliar, destino)

        # Passo 2: Mover disco maior para destino
        print(f'Mova o disco de {origem} para {destino}.')

        # Passo 3: Mover n - 1 discos do auxiliar para destino
        torreDeHanoi(n - 1, auxiliar, destino, origem)

torreDeHanoi(3, 'A', 'C', 'B')