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
        if posicao < self.tamanho and posicao >= 0:
            cont = 0
            var = self.inicio
            while var is not None:
                if cont == posicao:
                    return var.valor
                var = var.proximo
                cont += 1
        return None

    def remover(self, posicao):
        if (posicao < self.tamanho and posicao >= 0):
            if posicao == 0:
                if self.tamanho == 1:
                    self.fim =  None
                self.inicio = self.inicio.proximo
            else:
                aux = self.inicio
                for i in range(posicao - 1):
                    aux = aux.proximo
                if aux.proximo == self.fim:
                    self.fim = aux
                aux.proximo = aux.proximo.proximo
            self.tamanho -= 1
            return True
        else:
            return False

    # 1. Método que retorna o número de elementos
    def tamanho_lista(self):
        return self.tamanho

    # 2. Método que compara se duas listas são iguais
    def listas_iguais(self, outra):
        if self.tamanho != outra.tamanho:
            return False
        no1 = self.inicio
        no2 = outra.inicio
        while no1 is not None and no2 is not None:
            if no1.valor != no2.valor:
                return False
            no1 = no1.proximo
            no2 = no2.proximo
        return True

    # 3. Método que imprime os valores de trás para frente
    def imprimir_reverso(self):
        def empilhar(nodo):
            if nodo is not None:
                empilhar(nodo.proximo)
                print(nodo.valor)
        empilhar(self.inicio)


# lista = ListaEnc()
# lista.inserir(0, 'A')
# lista.inserir(1, 'B')
# lista.inserir(2, 'C')
# lista.inserir(0, 'D')
# lista.inserir(2, 'E')
# lista.imprimir()
# print('-----------')
# print(lista.verificaPosicao(0))
# print('------------')
# lista.remover('A')
# print(lista)

lista1 = ListaEnc()
lista1.inserir(0, 1)
lista1.inserir(1, 2)
lista1.inserir(2, 3)

lista2 = ListaEnc()
lista2.inserir(0, 1)
lista2.inserir(1, 2)
lista2.inserir(2, 3)

print("Tamanho da lista1:", lista1.tamanho_lista())
print("As listas são iguais?", lista1.listas_iguais(lista2))

print("Impressão reversa da lista1:")
lista1.imprimir_reverso()
