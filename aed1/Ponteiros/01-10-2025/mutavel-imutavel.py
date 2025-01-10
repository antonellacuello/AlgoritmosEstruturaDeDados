texto = "oi"
print(texto, id(texto))    #endereço da var
texto += "tchau"
print(texto, id(texto))    #string é imutavel, logo o endereço muda ao concatena-la

mensagem = 'oi'
outram = mensagem          #o python reconhece que as variaveis possuem o mesmo conteudo e aloca elas no mesmo endereço
print(mensagem, id(mensagem))
print(outram, id(outram))
mensagem += 'tchau'        #ao modificar a primeira variaveis o seu endereço mudou, mas a segunda variavel que era uma copia da primeira permaneceu com aquele endereço 
print(mensagem, id(mensagem))
print(outram, id(outram))