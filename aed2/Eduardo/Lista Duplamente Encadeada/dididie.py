class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, dado):
        novo_no = No(dado)
        if self.inicio:
            self.inicio.anterior = novo_no
            novo_no.proximo = self.inicio
        self.inicio = novo_no

    def inserir_fim(self, dado):
        if self.inicio is None:
            self.inserir_inicio(dado)
            return
        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo
        novo_no = No(dado)
        atual.proximo = novo_no
        novo_no.anterior = atual

    def inserir_posicao(self, posicao, dado):
        if posicao <= 0:
            self.inserir_inicio(dado)
            return

        atual = self.inicio
        index = 0

        while atual and index < posicao:
            atual = atual.proximo
            index += 1

        if atual is None:
            self.inserir_fim(dado)
        else:
            novo_no = No(dado)
            anterior = atual.anterior
            novo_no.proximo = atual
            novo_no.anterior = anterior
            atual.anterior = novo_no
            if anterior:
                anterior.proximo = novo_no
            else:
                self.inicio = novo_no

    def remover(self, dado):
        atual = self.inicio
        while atual and atual.dado != dado:
            atual = atual.proximo
        if not atual:
            print(f"Elemento {dado} não encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.inicio = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
        print("None")