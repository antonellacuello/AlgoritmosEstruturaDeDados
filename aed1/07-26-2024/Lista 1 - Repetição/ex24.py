# 24. Em uma competição de ginástica, cada atleta recebe votos de SETE jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça um programa em Python que receba o nome do(a) ginasta, e as notas de sua apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e a pior nota para calcular a média). As notas não são informadas em ordem (crescente ou decrescente).

nome = input('Insira o nome da ginasta: ')
nota = float(input('Digite a nota: '))
soma_notas = nota
nmax = nota
nmin = nota
c = 0

while c < 6:
	nota = float(input('Digite a nota: '))
	soma_notas += nota
	if nota >= nmax:
		nmax = nota
		print(nmax, nmin)
	if nota < nmin:
		nmin = nota
		print(nmax, nmin)	
	c += 1

soma_notas -= (nmax + nmin)
media = soma_notas / 5

print(f'A maior nota da ginasta {nome} foi {nmax}, e a menor nota foi {nmin}. A média de suas notas foi {media}')
