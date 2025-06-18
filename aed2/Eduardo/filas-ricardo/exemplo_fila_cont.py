from carro import *
from Fila_Cont import *


f= Fila(3)

print(f.consultar())
print(f.vetor)
print(f)
f.inserir(Carro("AAA1A11",2020))
print(f.consultar())
print(f.vetor)
print(f)
f.inserir(Carro("BBB2B22",2010))
print(f.consultar())
print(f.vetor)
print(f)
f.inserir(Carro("CCC2C22",2015))
print(f.consultar())
print(f.vetor)
print(f)

f.excluir()
print(f.consultar())
print(f.vetor)
print(f)