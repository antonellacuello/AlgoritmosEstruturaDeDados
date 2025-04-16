class Lista:
    def __init__ (self,max):  #inicia os atributos da classe (constructor - aloca espaço na memória p o obj) (self - é da classe)
        self.max = max         #var interna tem self na frente, pois é atributo da classe
        self.vetor = [None] * self.max   #todos os espaços começam como none 
        self.ini = None        #-1
        self.fim = None        #-1
    
    def __repr__ (self):
        string = '[ini '
        for i in range(self.ini, self.fim+1) :
            string = string + ' --> ' + str(self.vetor[i])
        return string + ']'

    def Vazia (self):
        return self.ini == None or self.fim == None   #troquei o -1   
    
    def Tamanho (self):
        if self.Vazia():
            return 0 
        else:
            return self.fim - self.ini + 1
    
    def Valor(self, posicao):
        if not self.Vazia() and posicao < self.Tamanho() and posicao >= 0:
            return self.vetor[self.ini + posicao]
        else:
            return 'O vetor não possui essa posição.'

    def Posicao(self, valor):
        for i in range(self.ini, self.fim + 1):
            if valor == self.vetor[i]:
                return i - self.ini
        return 'O valor não está presente no vetor. Não insista.'

    def Limpar (self):
        self.ini = None
        self.fim = None

    def Excluir (self):
        return 0

    def Inserir (self, posicao, dado):
        #verificar se existe espaço e se a posição é valida
        if posicao > 0 and posicao <= self.Tamanho() and self.Tamanho() < self.max:
            if self.Vazia():
                self.ini = self.max // 2
                self.fim = self.max // 2
                self.vetor[self.ini] = valor
            elif posicao == 0 and self.ini != 0: # se tem espaço, deslocar para o inicio
                self.ini = self.ini - 1
                self.vetor[self.ini] = valor
            elif posicao == self.Tamanho() and self.fim != self.max - 1:
                self.fim += 1
                self.vetor[self.fim] = valor
            elif self.fim == self.max - 1:
                for i in range(self.ini , self.ini + posicao):
                    self.vetor[i] = self.vetor[i + 1]
                self.vetor[self.ini + posicao] = valor
            else:
                self.fim = self.fim + 1
                for i in range(self.fim, self.ini + posicao):
                    vetor[i] = self.vetor[i - 1]
                self.vetor[self.ini + posicao] = valor
        else:
            return False

    # def Inserir (self, posicao, dado):
    #     #verificar se existe espaço e se a posição é valida
    #     if ((self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.Tamanho()):
    #         if (self.Vazia()):
    #             self.ini = 0
    #             self.fim = 0

    #         elif (self.fim != self.max - 1): # se tem espaço, deslocar para o fim
    #             for i in range(self.fim, self.ini + posicao - 2, -1):
    #                 self.vetor[i+1] = self.vetor[i]
    #                 print('moveu')

    #             self.fim = self.fim + 1

    #         else : # deslocar para o inicio
    #             for i in range(self.ini, self.ini + posicao):
    #                 self.vetor[i-1] = self.vetor[i]
    #                 print('moveu')

    #             self.ini = self.ini - 1]

    #         self.vetor[self.ini + posicao] = dado

    #         return True
    #     else:
    #         return False