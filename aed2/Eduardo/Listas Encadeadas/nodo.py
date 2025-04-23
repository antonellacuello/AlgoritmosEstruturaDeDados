class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEnc:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserir(self, posicao, valor):
        if posicao >= 0:
            if self.tamanho == 0:
                aux = Nodo(valor)
                self.inicio = aux
                self.fim =  aux
                self.tamanho += 1
            elif posicao == self.tamanho:
                aux = Nodo(valor)
                self.fim.proximo = aux
                self.fim = aux
                self.tamanho += 1
            elif posicao == 0:
                aux = Nodo(valor)
                aux.proximo = self.inicio
                self.inicio = aux
                self.tamanho += 1
            else:
                aux = Nodo(valor)
                var = self.inicio
                for i in range(posicao):
                    anterior = var
                    var = var.proximo
                aux.proximo = var
                anterior.proximo = aux
                self.tamanho += 1
            return True
        else:
            return False
    def imprimir(self):
        if self.inicio != None:
            var = self.inicio
            while var.proximo != None:
                print(var.valor)
                var = var.proximo
            if var.proximo == None:
                print(var.valor)
        else:
            print('Lista vazia.')
    def verificaPosicao(self, posicao):
        if posicao <= self.tamanho:
            cont = 0
            var = self.inicio
            if var != None:
                while var.proximo != None:
                    if cont == posicao:
                        return var.valor
                    var = var.proximo
                    cont += 1
                if var.proximo == None:
                    return var.valor
    #def verificaValor(self, valor):
    


lista = ListaEnc()
lista.inserir(0, 'A')
lista.inserir(1, 'B')
lista.inserir(2, 'C')
lista.inserir(0, 'D')
lista.inserir(2, 'E')
lista.imprimir()
print('-----------')
print(lista.verificaPosicao(0))