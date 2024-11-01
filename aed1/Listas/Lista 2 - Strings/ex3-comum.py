# 3. Escreva uma função que receba duas listas do usuário e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.
#for item in l1:
#    if item in l2:
#        comum.append(item)

#print(comum)    

def contem(teste, lista):
    for item in lista:
        if  teste == item:
            return True
    return False


def emComum(l1, l2):
    comum = []
    for item in l1:
        if contem(item, l2):
            comum.append(item)
    return comum

l1 = ['a', 'b', 'c', 't']
l2 = ['t', 'a', 'b']
comum = emComum(l1, l2)
print(comum)