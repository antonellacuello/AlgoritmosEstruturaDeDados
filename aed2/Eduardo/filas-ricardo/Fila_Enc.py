class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
    def __repr__(self):
        return str(self.info) + " | " + str(self.prox)

class FilaEnc:
    def __init__(self):
        self.ini = None
        self.fim = None

    def __repr__(self):
        return "[ ini --> " + str(self.ini) + "]"  

    def vazia(self):
        return self.ini == None

    def inserir(self, dado):
        novo = Nodo(dado)
        if self.vazia():
            self.ini = novo
        else:
            self.fim.prox = novo
        self.fim = novo

    def excluir(self):
        if (not self.vazia()):
            self.ini = self.ini.prox

    def consultar(self):
        if (not self.vazia()):
            return self.ini.info

    def destruir(self):
        while (not self.vazia()):
            self.excluir()