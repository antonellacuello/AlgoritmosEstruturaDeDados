# Verificação de senha

senha = input('Para acessar, digite a senha: ')

while senha != 'aed1':
	print('Senha incorreta. Tente novamente!')
	senha = input('Digite a senha: ')
print('Senha correta. Seja bem-vindo ao sistema!')

# Verificação de senha com limite de tentativas

senha = 'aed1'
c = 0
tentativa = input('Digite a senha: ')

while c != 3:
	c = c + 1
	if tentativa != senha:
		print('Senha incorreta. Tente novamente! \n')
		tentativa = input('Digite a senha: ')

if tentativa == senha:
	print('Senha correta. Seja bem-vindo ao sistema!')
