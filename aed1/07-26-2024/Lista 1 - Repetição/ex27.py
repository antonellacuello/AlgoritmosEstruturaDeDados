# Faça um programa em python que desenhe uma pirâmide conforme 2 dados informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade de andares.
'''Ex: 	Informe o tijolo: A
	Informe a quantidade de andares: 5

        A
       AAA
      AAAAA
     AAAAAAA
    AAAAAAAAA
'''

h = int(input('Informe a altura da escadinha: '))
e = input('Do que a escadinha será feita? ')
ch = 1
cspace = h - 1

while ch <= h:
	print((' ' * cspace) + ((e + ' ') * ch))
	ch += 1
	cspace -= 1
