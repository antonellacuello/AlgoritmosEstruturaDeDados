from carro import *
from ListaCont import *

carroA = Carro('AAA123', 2020)
carroB = Carro('BBB456', 2009)
carroC = Carro('CCC789', 1985)

lista = Lista(5)
if (lista.Inserir(1,carroA)) :
    print(lista)
if (lista.Inserir(1,carroB)) :
    print(lista)
if (lista.Inserir(1,carroC)) :
    print(lista)
if (lista.Inserir(1,carroA)) :
    print(lista)
if (lista.Inserir(1,carroB)) :
    print(lista)
if (lista.Inserir(5,carroC)) :
    print(lista)

meuCarro = lista.Consultar(1)
print(meuCarro)