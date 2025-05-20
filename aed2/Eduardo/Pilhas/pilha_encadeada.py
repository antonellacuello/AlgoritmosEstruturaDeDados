'''class Nodo:
    def __init__(self, dado):
        self.info = dado
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def Vazia(self):
        return self.topo is None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if not self.Vazia():
            novo.prox =  self.topo
        self.topo = novo

    def Excluir(self):
        if not self.Vazia():
            self.topo = self.topo.prox

    def Consultar(self):
        if not self.Vazia():
            return self.topo.info
        
    def Destruir(self):
        while not self.Vazia():
            self.Excluir()
    
    def Inverter(pilha):
        invertida = Pilha()
        
        while not pilha.Vazia():
            dado = pilha.Consultar()
            invertida.Empilhar(dado)
            pilha.Excluir()

        while not invertida.Vazia():
            dado = invertida.Consultar()
            pilha.Empilhar(dado)
            invertida.Excluir()

        return invertida

    def TesteIgualdade(p1, p2):
        atual1 = p1.topo
        atual2 = p2.topo

        while atual1 is not None and atual2 is not None:
            if atual1.info != atual2.info:
                return False
            atual1 = atual1.prox
            atual2 = atual2.prox

        return atual1 is None and atual2 is None

    def MenorElemento(self):
        if self.Vazia():
            return None

        atual = self.topo
        menor = atual.info

        while atual is not None:
            if atual.info < menor:
                menor = atual.info
            atual = atual.prox

        return menor

print("== Teste de Inversão ==")
p = Pilha()
p.Empilhar(1)
p.Empilhar(2)
p.Empilhar(3)

#p.Inverter()

while not p.Vazia():
    print(p.Consultar())
    p.Excluir()

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
print(p1.MenorElemento())'''

class Nodo:
    def __init__(self, dado):
        self.info = dado
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def Vazia(self):
        return self.topo is None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if not self.Vazia():
            novo.prox =  self.topo
        self.topo = novo

    def Excluir(self):
        if not self.Vazia():
            self.topo = self.topo.prox

    def Consultar(self):
        if not self.Vazia():
            return self.topo.info
        
    def Destruir(self):
        while not self.Vazia():
            self.Excluir()
    
    def Inverter(pilha):
        invertida = Pilha()
        
        while not pilha.Vazia():
            dado = pilha.Consultar()
            invertida.Empilhar(dado)
            pilha.Excluir()

        return invertida


    def TesteIgualdade(p1, p2):
        atual1 = p1.topo
        atual2 = p2.topo

        while atual1 is not None and atual2 is not None:
            if atual1.info != atual2.info:
                return False
            atual1 = atual1.prox
            atual2 = atual2.prox

        return atual1 is None and atual2 is None

    def MenorElemento(self):
        if self.Vazia():
            return None

        atual = self.topo
        menor = atual.info

        while atual is not None:
            if atual.info < menor:
                menor = atual.info
            atual = atual.prox

        return menor

    def Printar(self):
        aux = Pilha()

        if self.Vazia():
            print("Pilha vazia.")
            return

        elementos = []
        while not self.Vazia():
            dado = self.Consultar()
            elementos.append(str(dado)) 
            aux.Empilhar(dado)
            self.Excluir()
        
        # Imprime os elementos na ordem correta (topo para base)
        print(" -> ".join(elementos))

        while not aux.Vazia():
            self.Empilhar(aux.Consultar())
            aux.Excluir()

# ========== TESTES ==========

print("== Teste de Inversão ==")
p = Pilha()
p.Empilhar(3)
p.Empilhar(2)
p.Empilhar(1)
'''while not p.Vazia():
    print(p.Consultar())
    p.Excluir()'''
#print("Pilha antes da inversão (do topo para a base):")
#p.Printar() # Saída: 1 -> 2 -> 3

inv = p.Inverter() # A pilha 'p' é invertida no lugar
while not inv.Vazia():
    print(inv.Consultar())
    inv.Excluir()
#print("\nPilha após a inversão (do topo para a base):")
#p.Printar() # Saída: 3 -> 2 -> 1