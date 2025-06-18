class Fila:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.li = 0
        self.ls = tamanho - 1
        self.ini = self.li - 1
        self.fim = self.ls + 1
        
       
    def vazia(self):
        return self.ini < self.li or self.fim > self.ls
    
    def cheia(self):
        return (self.ini== self.li and self.fim == self.ls) or (self.ini == self.fim+1)
    
    def inserir(self, dado):
        if (self.vazia()):
            self.ini = self.li
            self.fim = self.li
            self.vetor[self.fim] = dado
        elif(not self.cheia()):
            if (self.fim == self.ls):
                self.fim = self.li
            else:
                self.fim += 1
            self.vetor[self.fim] = dado
    
    def excluir(self):
        if (not self.vazia()):
            if (self.ini > self.fim and self.ini == self.ls):
                self.ini = self.li
            elif(self.ini == self.fim):
                self.destruir()
            else:
                self.ini += 1        
    
    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1

    def consultar(self):
        if (not self.vazia()):
            return self.vetor[self.ini]
        
    def __repr__(self):
        string = "["
        if (not self.vazia()):
            if (self.ini <= self.fim):
                for i in range(self.ini, self.fim + 1):
                    string = string + " --> " + str(self.vetor[i])
            else:
                for i in range(self.ini, self.ls + 1):
                    string = string + " --> " + str(self.vetor[i])
                for i in range(self.li, self.fim + 1):
                    string = string + " --> " + str(self.vetor[i])
        return string + "]" 

