class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    # def __repr__(self):
    #     return 
class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def __repr__(self):
        return "[ inicio --> " + str(self.inicio) + ", fim --> " + str(self.fim) + " ]"

    def vazia(self):
        return self.inicio is None
    
    def consultar(self):
        if not self.vazia():
            return 'Dado no início da fila: ' + str(self.inicio.dado)
        return 'Fila vazia! Não há dados para serem consultados.'
    
    def inserir(self, dado):
        novo_nodo = Nodo(dado)
        if self.vazia():
            self.inicio = novo_nodo
        else:
            self.fim.proximo = novo_nodo
        self.fim = novo_nodo
        return 'Dado inserido com sucesso!'
    
    def excluir(self):
        if not self.vazia():
            self.inicio = self.inicio.proximo
    
    def destruir(self):
        self.inicio = None
        self.fim = None
        return 'Fila destruída!'