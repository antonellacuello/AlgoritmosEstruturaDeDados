def incrementaImutavel(x):
    print(x, id(x))  #antes de incrementar a variavel local possui o mesmo endereço da variavel global
    x += 1
    print(x, id(x))  #aqui o endereço ja muda (variavel local)

x = 15               #global
print(x, id(x))
incrementaImutavel(x)        #global
print(x, id(x))      #local

def incrementaMutavel(y):  #como listas são mutáveis usam o mesmo slot de memória, as funções criam variáveis novas mas apontam para o mesmo slot
    print(y, id(y))        #global
    y[0] += 1
    print(y, id(y))        #global

y = [15]
print(y, id(y))            #global
incrementaMutavel(y)
print(y, id(y))            #global