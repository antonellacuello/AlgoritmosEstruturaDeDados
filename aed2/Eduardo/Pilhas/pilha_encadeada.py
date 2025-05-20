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