# EXERCÍCIOS DE ARQUIVOS - 06/12/2024
# 1) Faça uma função que recebe um código de estado e retorne quantas cidades há para aquele código.
'''def numCidadesDoCod(lista, cod_uf):
    num_cidades = 0
    for linha in lista:
        coluna = linha.split(',')
        if coluna[0] == cod_uf:
            num_cidades += 1
    return num_cidades
            

arq = open('municipios.csv', 'r')
dados = arq.readlines()
cod_uf = input('Insira o código de Estado: ')
num_cidades = numCidadesDoCod(dados, cod_uf)
print(f'Existem {num_cidades} cidades com o código de Estado {cod_uf}.')
arq.close()'''

# 2) Faça uma função que recebe uma string e retorne quais cidades contem a string. EX: 'rio' -> Rio Grande, Rio de Janeiro...
def contemPalavra(dados, palavra):
    lista_cidades = []
    for linha in dados:
        coluna = linha.split(',')
        posicao = coluna[2].find(palavra)
        if posicao != -1:
            lista_cidades.append(coluna[2])
    cidades = ''.join(lista_cidades)
        #if palavra in coluna[2]:
            #cidades.append(coluna[2])
    return cidades


arq = open('municipios.csv', 'r')
dados = arq.readlines()
palavra = input('Digite a palavra que deseja buscar: ').capitalize()
cidades = contemPalavra(dados, palavra)
print(f'Cidades que contem a palavra "{palavra}": \n{cidades}')
arq.close()

# 3) Semelhante a 2, porém, retorna o número de cidades.
'''def contemPalavra(dados, palavra):
    num_cidades = 0
    for linha in dados:
        coluna = linha.split(',')
        posicao = coluna[2].find(palavra)
        if posicao != -1:
            num_cidades += 1
    return num_cidades


arq = open('municipios.csv', 'r')
dados = arq.readlines()
palavra = input('Digite a palavra que deseja buscar: ').capitalize()
num_cidades = contemPalavra(dados, palavra)
print(f'Cidades que contem a palavra "{palavra}": {num_cidades}')
arq.close()'''