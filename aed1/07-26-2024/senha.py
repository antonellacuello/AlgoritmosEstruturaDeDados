# Verificação de senha com limite de tentativas

senha = 'aed1'
c = 0
tentativa = input('Digite a senha: ')

while c != 5:
	c = c + 1
	if tentativa != senha:
		print('Senha incorreta. Tente novamente! \n')
		tentativa = input('Digite a senha: ')

if tentativa == senha:
	print('Senha correta. Seja bem-vindo ao sistema!')
else:
	print('Limite de tentativas atingido. Desista.')
