MULTIPLICA()
int op1[4], op2[4], produto[7][4];
produto = [
	[ 0,  0,  0,  0],
	[ 0,  0,  0,  0],
	[ 0,  0,  0,  0],
	[ 0,  0,  0,  0]
       ]
write('Informe o primeiro operando: ');
read(op1);
write('Informe o segundo operando: ');
read(op2);

a = 0 
while a != 3:
	for i = 3 downto 0
		for j = 3 downto 0
			produto[a][i] = int(op1[i]) * int(op2[j])
		a += 1