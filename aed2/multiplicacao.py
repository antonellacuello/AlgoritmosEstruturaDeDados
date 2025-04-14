MULTIPLICA()
int op1[4], op2[4], resto[4], aux[2], produto[7];

write('Informe o primeiro operando: ');
read(op1);
write('Informe o segundo operando: ');
read(op2);

a = 0;
pp = -1;
shift = -1
while a != 3:
	pp = -1 + (a * shift)
	resto = [0, 0, 0, 0]
	for i = 3 downto 0
		aux = op2[i] * op1[i]
		if resto[i] != 0:
			aux += resto[i]
		if aux >= 10:
			resto[i - 1] = aux[0]
		produto[pp] += aux[1]
		pp += -1
	a += 1
