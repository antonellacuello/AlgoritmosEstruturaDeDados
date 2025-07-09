class Tabela:
    def __init__(self, tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.ini = self.li - 1
        self.fim =self.ls + 1

    def __repr__(self):
        string = ""
        if (not self.vazia()):
            for i in range(self.ini, self.fim + 1):
                string = string + str(self.chave[i]) + ": {" + str(self.valor[i]) + "}\n"
        return string + "\n" 
    
    def vazia(self):
        return (self.ini < self.li)
    
    def cheia(self):
        return (self.ini == self.li and self.fim == self.ls)

    def buscar(self, chave):
        if not self.vazia():
            for i in range(self.ini,self.fim+1):
                if self.chave[i] == chave:
                    return i
        return None
    
    def inserir(self, chave, valor):
        posicao = self.buscar(chave)
        if posicao is not None:
            self.valor[posicao] = valor
        elif (not self.cheia()):
            if(self.vazia()):
                self.ini=self.li
                self.fim=self.li
            else:
                self.fim += 1
            self.chave[self.fim] = chave
            self.valor[self.fim] = valor
    
    def consultar(self, chave):
        posicao = self.buscar(chave)
        if posicao is not None :
            return self.valor[posicao]
        else: 
            return None    

    def excluir(self, chave):
        posicao = self.buscar(chave)
        if posicao is not None:
            for i in range(posicao, self.fim):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.fim -= 1

    def destruir(self):
        self.ini=self.li-1
        self.fim=self.ls+1

'''
t = Tabela(10)
t.inserir(17, "A")
t.inserir(5, "B")
t.inserir(30, "C")
t.inserir(5, "D")
t.inserir(11, "E")

print(t)
print(t.consultar(5))

t.excluir(30)
t.inserir(55, "F")
print(t)

'''