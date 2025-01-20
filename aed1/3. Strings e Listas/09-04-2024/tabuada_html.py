print('<h1>TABUADAS DO 1 AO 10</h1>')
t = 10
c1 = 1
t1 = 1

print('<table border=1>')
while c1 <= t:
	c = 1
	r = 0
	print(f'<h2>TABUADA DO {t1}</h2>')
	while c <= 10:
		r = c * t1
		print(f'<caption>TABUADA DO {t1}</caption>')
		print('<tr>')
		print(f'<td>{c} X {t1}</td>')
		print(f'<td>{r}</td>')
		print('</tr>')
		c += 1
	c1 += 1
	t1 += 1
print('</table>')
