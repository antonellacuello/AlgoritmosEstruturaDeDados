arq = open('alunos.csv', 'r')

# exercício 1 - mostre todos os dados
'''alunos = arq.read()
print(alunos)'''

# exercício 2 - liste apenas os nomes
'''lista_alunos = arq.readlines()
for linha in lista_alunos:
    colunas = linha.split(';')
    print(colunas[1])'''

# exercício 3 - mostre quem é o aluno mais novo
alunos = arq.readlines()
datas = []
for linha in alunos[1:]:
    coluna = linha.split(';')
    datas.append(coluna[2])

anos = []
for data in datas:
    ano = ''
    i = 0
    while i < len(data):
        if i == 6 or i == 7 or i == 8 or i == 9:
            ano += data[i]
        i += 1
        
    anos.append(int(ano))

mais_novo = max(anos)
ano_mais_novo = str(mais_novo)
for linha in alunos[1:]:
    coluna = linha.split(';')
    if ano_mais_novo in coluna[2]:
        nome_mais_novo = coluna[1]
print('O aluno mais novo é: ' + nome_mais_novo)