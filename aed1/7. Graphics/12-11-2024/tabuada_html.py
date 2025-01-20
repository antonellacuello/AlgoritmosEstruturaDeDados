'''with open('saida.html', 'w') as arq:
	tab_final = int(input('Até qual tabuada deseja visualizar? '))
	print('Tabela gerada com sucesso!')
	c1 = 1
	tab_atual = 1
	arq.write(f'<h1>TABUADAS DO 0 AO {tab_final}</h1>')

	arq.write('<table border=1>')
	while c1 <= tab_final:
		multiplicador = 1
		resposta = 0
		arq.write(f'<h2>TABUADA DO {tab_atual}</h2>')
		while multiplicador <= 10:
			resposta = multiplicador * tab_atual
			arq.write(f'<caption>TABUADA DO {tab_atual}</caption>')
			arq.write('<tr>')
			arq.write(f'<td>{multiplicador} X {tab_atual}</td>')
			arq.write(f'<td>{resposta}</td>')
			arq.write('</tr>')
			multiplicador += 1
		c1 += 1
		tab_atual += 1
	arq.write('</table>')'''

# jeito prisco
tab_final = int(input('Até qual tabuada deseja visualizar? '))
print('Tabela gerada com sucesso!')
saida = 'Tabuadas!<hr>'

for tab_atual in range(tab_final + 1):
	saida += '<table border=1>'
	for multiplicador in range(11):
		resultado = multiplicador * tab_atual
		saida += f'<tr><td>{multiplicador} x {tab_atual} =</td> <td>{resultado}</td> </tr>'

	saida += '</table><br>'

with open('saida.html', 'w') as arq:
	arq.write(saida)
