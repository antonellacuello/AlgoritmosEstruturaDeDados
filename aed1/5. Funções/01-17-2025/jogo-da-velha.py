#9 lista de revisao
def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    return None

def imprimir_tabuleiro(tabuleiro):
    print(f"\n     1   2   3")
    print(f"A    {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print(f"    -----------")
    print(f"B    {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print(f"    -----------")
    print(f"C    {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}\n")

def posicao_valida(posicao, tabuleiro):
    linhas = {'a': 0, 'b': 1, 'c': 2}
    if len(posicao) == 2 and posicao[0].lower() in linhas and posicao[1] in '123':
        linha = linhas[posicao[0].lower()]
        coluna = int(posicao[1]) - 1
        if tabuleiro[linha][coluna] == ' ':
            return linha, coluna
    return None

def main():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    print(f'---------------------------------------\n| Bem vindo ao JOGO DA VELHA de AED1! | \n---------------------------------------')
    print(f'O primeiro jogador será o X e o segundo será o O.\n')

    vencedor = None
    jogadas = 0

    while jogadas < 9 and vencedor is None:
        imprimir_tabuleiro(tabuleiro)
        posicao = input(f"Jogador {jogador_atual}, informe a posição (exemplo: a1): ").strip()
        valida = posicao_valida(posicao, tabuleiro)

        if valida:
            linha, coluna = valida
            tabuleiro[linha][coluna] = jogador_atual
            vencedor = verificar_vencedor(tabuleiro)
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            jogadas += 1
        else:
            print("Posição inválida ou já ocupada. Tente novamente.")

    imprimir_tabuleiro(tabuleiro)

    if vencedor:
        print(f"Parabéns! O jogador {vencedor} venceu!\n")
    else:
        print("O jogo terminou em empate!\n")

if __name__ == "__main__":
    main()
