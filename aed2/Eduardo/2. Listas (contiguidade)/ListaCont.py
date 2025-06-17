class Lista:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def __repr__(self):
        string = "[ini "
        for i in range(self.ini, self.fim + 1):
            string = string + " -> " + str(self.vetor[i])
        return string + "]" 

    def __str__(self):
        string = "max: " + str(self.max) + ", vetor: [ "
        for i in range(0, self.max):
            string = string + str(i) + ": " + str(self.vetor[i]) + "-> "
        return string + "] ini: " + str(self.ini) + ", fim: " + str(self.fim)

    def Vazia(self):
        return self.ini == -1 or self.fim == -1

    def Tamanho(self):
        if self.Vazia():
            return 0
        else: 
            return self.fim - self.ini + 1

    def Inserir(self, posicao, dado):
        # verificar se existe espaço e se a posição é válida
        if ((self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.Tamanho()+1):
            if (self.Vazia()):
                self.ini = self.max // 2
                self.fim = self.max // 2
            elif (self.fim != self.max - 1): # se tem espaço, deslocar para o fim 
                for i in range(self.fim, self.ini + posicao -2, -1):
                    self.vetor[i+1] = self.vetor[i]
                    print("moveu")
                self.fim = self.fim + 1
            else: # deslocar para o início
                for i in range(self.ini, self.ini + posicao - 1): 
                    self.vetor[i-1] = self.vetor[i]
                    print("moveu")
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            return False
    
    def Consultar(self, posicao):
        if not self.Vazia():
            return self.vetor[self.ini + posicao - 1]

    def Limpar(self):
        self.ini = -1
        self.fim = -1
    
    def Excluir(self):
        return 0



    def InserirOtimizado(self, posicao, dado):
        # verificar se existe espaço e se a posição é válida
        if (self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.Tamanho()+1:
            if (self.Vazia()):
                self.ini = self.max // 2
                self.fim = self.max // 2
                indice = self.ini
            # se for no início e exitir espaço
            elif posicao == 1 and self.ini != 0:
                self.ini = self.ini - 1
                indice = self.ini
            # se for no fim e existir espaço
            elif posicao > self.Tamanho() and self.fim != self.max - 1:
                self.fim = self.fim + 1
                indice = self.fim
            else:
                # se não tem espaço no início, ou se custo é menor deslocando para o fim e ainda existe espaço
                if self.ini == 0 or (posicao > self.Tamanho() // 2 and self.fim != self.max - 1):
                    for i in range(self.fim, self.ini + posicao - 2, -1): # deslocar para o fim
                        self.vetor[i+1] = self.vetor[i]
            #            print("moveu")
                    self.fim = self.fim + 1
                else: # deslocar para o início
                    for i in range(self.ini, self.ini + posicao - 1):
                        self.vetor[i-1] = self.vetor[i]
            #            print("moveu")
                    self.ini = self.ini - 1
            indice = self.ini + posicao - 1
            self.vetor[indice] = dado
            return True
        else:
            return False

    def RemoverOtimizado(self, posicao):
        if self.Vazia() or posicao <= 0 or posicao > self.Tamanho():
            return False

        indice = self.ini + posicao - 1

        if self.Tamanho() == 1:
            self.ini = -1
            self.fim = -1
            return True

        meio = self.Tamanho() // 2

        if posicao <= meio:
            # Deslocar para a direita (da esquerda para o centro)
            for i in range(indice, self.ini, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.ini += 1
        else:
            # Deslocar para a esquerda (do centro para o fim)
            for i in range(indice, self.fim):
                self.vetor[i] = self.vetor[i + 1]
            self.fim -= 1

        return True
