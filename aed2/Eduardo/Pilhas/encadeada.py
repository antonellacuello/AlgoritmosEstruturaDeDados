class Pilha:
    def __init__(self):
        self.topo = None

    def Empilhar(self, dado):
        novo = Nodo(dado)
        if not self.vazia():
            novo.prox =  self.topo
        self.topo = novo

    def Excluir(self):
        if not self.vazia():
            self.topo = self.topo.prox

    def Consultar(self):
        if not self.vazia():
            return self.topo.info
        
    def Destruir(self):
        while not self.vazia():
            self.Excluir()

    #implementar função das classes invertidas, comparação e menor elemento