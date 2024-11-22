def mostrarNomes(lista):
    for linha in lista[1:]:
        nomes = linha.split(';')
        print(nomes[1])

def maisNovo(lista):
    novo = '10251231'
    nome_do_novo = ''
    for linha in lista[1:]:
        uma_lista = linha.split(';')
        data = uma_lista[2][:-1]
        lista_data = data.split('/')
        data_padrao = lista_data[2] + lista_data[1] + lista_data[0]
        if data_padrao > novo:
            novo = data_padrao
            nome_do_novo = uma_lista[1]
            dt_original = data
    print(nome_do_novo, dt_original)

arq = open('alunos.csv', 'r')
dados = arq.readlines()
maisNovo(dados)
mostrarNomes(dados)