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
    
    def Inverter(self):
        invertida = Pilha()

        while not self.Vazia():
            dado = self.Consultar()
            invertida.Empilhar(dado)
            self.Excluir()

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
            elementos.append(str(dado)) # Coleta os elementos para imprimir
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

print("Pilha antes da inversão (do topo para a base):")
p.Printar() # Saída: 1 -> 2 -> 3

p.Inverter() # A pilha 'p' é invertida no lugar
print("\nPilha após a inversão (do topo para a base):")
p.Printar() # Saída: 3 -> 2 -> 1