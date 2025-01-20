# AULA DE STRINGS - 04/09/2024
# Listas: Tipo estruturado, armazenam qualquer coisa e são mutáveis.
# Strings: Tipo estruturado, armazenam CARACTERES e são IMUTÁVEIS.

'''compras = ['nutella', 'pão', 'queijo', 'coquinha', 'patê', 'carne']

compras[4] = 'brigadeiro'  # substitui o elemento daquela posição
compras.append('nescau')  # insere no fim da lista 
compras.insert(0, 'leite condensado') # insere na posição desejada sem retirar o elemento que já estava nessa posição
print(compras)  # função independente

i = 0
while i < len(compras):    # isto é uma ITERAÇÃO, porém existe um comando que ja faz isso o FOR
	print(compras[i])
	i += 1

for produto in compras:
	print(produto)

antonella = ['Antonella', 20, 1.63, 'Rio Grande', ['arroz', 'feijão', 'nhoque']]'''

# Listas -> Objeto; Python -> Programação Orientada a Objetos.
# PRINT: função independente; APPEND: Metódo, depende de algo.

# Exercício 1) Leia uma lista de compras ate que o usuário deixe um espaço vazio e imprima seus elementos

'''compras = []
produto = ' '

while produto != '':
	produto = input('Insira o produto: ')
	if produto == '':
		break
	else:
		compras.append(produto)

print(f'\nLISTA DE COMPRAS!')
for produto in compras:
	print(f'-> {produto}')

print(f'\nLISTA DE COMPRAS!')
i = 0
while i < len(compras):
	print(f'{i + 1}. {compras[i]}')
	i += 1'''

# EXERCICIO 2) Leia duas listas, uma com o produto e a outra com seu preço. Imprima um do lado do outro e a soma total.

produtos = []
produto = ' '
precos = []
preco = ' '
total = 0

while produto != '':
	produto = input('Insira o produto: ')
	preco = input('Insira o seu respectivo preco: ')
	if produto == '' or precos == '':
		break
	else:
		preco = float(preco)
		produtos.append(produto)
		precos.append(preco)
		total += preco

print(f'\nLISTA DE COMPRAS:')
i = 0
while i < len(produtos):
	print(f'{produtos[i]} -> {precos[i]}')
	i += 1
print('-----------------')
print(f'TOTAL: R${total}')
