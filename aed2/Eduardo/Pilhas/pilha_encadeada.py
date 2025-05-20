class Nodo:
    def __init__(self,dado):
        self.info=dado
        self.prox=None

class Pilha:
    def __init__(self):
        self.topo=None
    
    def vazia(self):
        return self.topo is None
    
    def Empilhar(self,dado):
        novo = Nodo(dado)
        if(not self.vazia()):
            novo.prox = self.topo
        self.topo = novo
    
    def Excluir(self):
        if(not self.vazia()):
            self.topo = self.topo.prox

    def Consultar(self):
        if(not self.vazia()):
            return self.topo.info
    
    def Destruir(self):
        while(not self.vazia()):
            self.Excluir




print("\n== Teste de Igualdade ==")
p1 = Pilha()
p2 = Pilha()
for valor in [3, 2, 1]:
    p1.Empilhar(valor)
    p2.Empilhar(valor)

print(Pilha.TesteIgualdade(p1, p2)) 

p2.Excluir()
print(Pilha.TesteIgualdade(p1, p2))

print("\n== Teste de Menor Elemento ==")
print(p1.MenorElemento())