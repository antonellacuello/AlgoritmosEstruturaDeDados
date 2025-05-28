# Fila por contiguidade física

class Fila:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.li = 0
        self.ls = tamanho - 1
        self.ini = self.li - 1
        self.fim = self.ls + 1
    def vazia(self):
        return self.ini < self.li and self.fim > self.ls
    def cheia(self):
        return (self.ini == self.li and self.fim == self.ls) or self.fim == self.ini - 1
    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1
        return 'Fila destruída!'
    def inserir(self, dado):
        if self.vazia():
            self.ini = self.li
            self.fim = self.li
            self.vetor[self.fim] = dado
        elif not self.cheia():
            if self.fim == self.ls:
                self.fim = self.li
            else:
                self.fim += 1
            self.vetor[self.fim] = dado
        else:
            return 'Fila cheia!'
        return 'Dado inserido com sucesso!'
    def excluir(self):
        # if self.vazia():
        #     return 'Fila vazia!'
        # dado = self.vetor[self.ini]
        # if self.ini == self.fim:
        #     self.ini = self.li - 1
        #     self.fim = self.ls + 1
        # elif self.ini == self.ls:
        #     self.ini = self.li
        # else:
        #     self.ini += 1
        # return 'Dado removido: ' + str(dado)
        if not self.vazia():
            dado = self.vetor[self.ini]
            if self.ini > self.fim and self.ini == self.ls:
                self.vetor[self.ini] = None
                self.ini = self.li
            elif self.ini == self.fim:
                self.destruir()
            else:
                self.ini += 1
            return 'Dado removido: ' + str(dado)
        return 'Fila vazia! Não há dados para serem excluídos.'
    def consultar(self):
        if not self.vazia():
            return 'Dado no início da fila: ' + str(self.vetor[self.ini])
        return 'Fila vazia! Não há dados para serem consultados.'