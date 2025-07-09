class Tabela:
    def __init__(self, quantidade):
        self.max = quantidade
        self.tam = 0
        self.chave = [None] * (self.max)
        self.valor = [None] * (self.max)
       
        
    def __str__(self):
        string = ""
        if self.tam > 0:
            for i in range(self.tam):
                string = string + str(self.chave[i]) + ": {" + str(self.valor[i]) + "}\n"
        return string + "\n" 

    def buscaLinear(self, chave):
        if self.tam > 0:
            for i in range(self.tam):
                if self.chave[i] == chave:
                    return i
        return None    

    def inserirFinal(self, chave, valor):
        posicao = self.buscar(chave)
        if posicao != None:
            self.valor[posicao] = valor
        elif self.tam < self.max:
            self.chave[self.tam] = chave
            self.valor[self.tam] = valor
            self.tam += 1
    
    def consultar(self, chave):
        posicao = self.buscar(chave)
        if posicao != None:
            return self.valor[posicao]
        else: 
            return None    

    def excluir(self, chave):
        posicao = self.buscar(chave)
        if posicao != None:
            for i in range(posicao, self.tam - 1):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.tam -= 1

    def limpar(self):
        self.tam = 0    

    def buscar(self, chave):
        return self.buscaLinear(chave)
        #return self.buscaBinaria(chave)
        #return self.buscaBinariaRecursiva(chave, 0, self.tam - 1)

    def inserir(self, chave, valor):
        #self.inserirFinal(chave, valor)
        self.inserirOrd(chave, valor)

    def inserirOrd(self, chave, valor):
        posicao = self.buscar(chave)
        if posicao != None:
            self.valor[posicao] = valor
        elif self.tam < self.max:
            i = 0
            while i < self.tam and self.chave[i] < chave:
                i += 1
            for j in range(self.tam, i, -1):
                self.chave[j] = self.chave[j-1]
                self.valor[j] = self.valor[j-1]
            self.chave[i] = chave
            self.valor[i] = valor
            self.tam += 1


    def buscaBinaria(self, chave):
        if self.tam > 0:
            ini = 0
            fim = self.tam - 1
            while (ini <= fim):
                meio = (ini + fim)//2
                if (self.chave[meio] == chave):
                    return meio
                elif (self.chave[meio] > chave):
                    fim = meio - 1
                else:
                    ini = meio + 1
        return None

    def buscaBinariaRecursiva(self, chave, ini, fim):
        if (self.tam == 0 or (ini == fim and self.chave[ini] != chave)):
            return None
        meio = (ini + fim)//2
        if (self.chave[meio] == chave):
            return meio
        elif (self.chave[meio] > chave):
            return self.buscaBinariaRecursiva(chave, ini, meio-1)
        else:
            return self.buscaBinariaRecursiva(chave, meio+1, fim)
        
   

t = Tabela(10)
t.inserir(17, "A")
t.inserir(5, "B")
t.inserir(30, "C")
t.inserir(5, "D")
t.inserir(11, "E")
t.excluir(50)
t.inserir(55, "F")
print(t)

#print(t.consultar(11))