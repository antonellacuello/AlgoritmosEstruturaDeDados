# 4. Crie um programa em Python que leia as notas do estudante nos 4 bimestres da nossa disciplina e a frequência (em porcentagem). A seguir informe se o estudante passou por média, rodou ou ficou em exame. Para passar por média, o estudante deve ter média maior ou igual a 7. Estudante com média abaixo de 3 roda sem ao menos fazer o exame. O estudante que tiver menos de 75% de frequência também está rodado na disciplina.

n1 = float(input('Insira sua nota do PRIMEIRO bimestre: '))	
n2 = float(input('Insira sua nota do SEGUNDO bimestre: '))
n3 = float(input('Insira sua nota do TERCEIRO bimestre: '))
n4 = float(input('Insira sua nota do QUARTO bimestre: '))
f = int(input('Insira sua FREQUÊNCIA, em porcentagem: '))

m = (n1 + n2 + n3 + n4) / 4

if m >= 7  and f >= 75:
	print('Aprovado!')
else:
	if m < 3 or f < 75:
		print('Reprovado. Sem direito a exame.')
	else:
		print('Realize ao exame.')
