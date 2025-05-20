class Pilha:
    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1

    def Inserir(self, dado):
        if self.topo < self.lim:
            self.topo += 1
            self.vetor[self.topo] = dado

    def Excluir(self):
        if self.topo >= self.base:
            self.topo -= 1

    def Consultar(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]
        return None
        
    def Destruir(self):
        self.topo = self.base - 1

    def Inverter(pilha):
        invertida = Pilha(pilha.lim + 1)
        while pilha.topo >= pilha.base:
            invertida.Inserir(pilha.Consultar())
            pilha.Excluir()
        return invertida
    
    def TesteIgualdade(p1, p2):
        if p1.topo != p2.topo:
            return False
        
        aux1 = Pilha(p1.lim + 1)
        aux2 = Pilha(p2.lim + 1)
        iguais = True

        while p1.topo >= p1.base and p2.topo >= p2.base:
            val1 = p1.Consultar()
            p1.Excluir()
            aux1.Inserir(val1)

            val2 = p2.Consultar()
            p2.Excluir()
            aux2.Inserir(val2)

            if val1 != val2:
                iguais = False

        while aux1.topo >= aux1.base:
            p1.Inserir(aux1.Consultar())
            aux1.Excluir()

        while aux2.topo >= aux2.base:
            p2.Inserir(aux2.Consultar())
            aux2.Excluir()
        
        return iguais

    def menorElemento(self):
        if self.topo < self.base:
            return None
        
        menor = self.vetor[self.base]
        for i in range(self.base, self.topo + 1):
            if self.vetor[i] is not None and self.vetor[i] < menor:
                menor = self.vetor[i]
        return menor


# ========== TESTES ==========

print("== Teste de Inversão ==")
pilha = Pilha(10)
pilha.Inserir(5)
pilha.Inserir(10)
pilha.Inserir(3)
invertida = Pilha.Inverter(pilha)
print("Limite:", invertida.lim)
print("Base:", invertida.base)
print("Valor Topo:", invertida.Consultar())
print("Topo:", invertida.topo)

print("\n== Teste de Igualdade ==")

p1 = Pilha(5)
p2 = Pilha(5)

p1.Inserir(1)
p1.Inserir(2)
p1.Inserir(3)

p2.Inserir(1)
p2.Inserir(2)
p2.Inserir(3)

resultado = Pilha.TesteIgualdade(p1, p2)
print("As pilhas são iguais?", resultado)

print("\n== Teste de Igualdade com Pilhas Diferentes ==")

p3 = Pilha(5)
p4 = Pilha(5)

p3.Inserir(1)
p3.Inserir(2)
p3.Inserir(3)

p4.Inserir(1)
p4.Inserir(2)
p4.Inserir(4)

resultado2 = Pilha.TesteIgualdade(p3, p4)
print("As pilhas são iguais?", resultado2)


print("\n== Teste de Menor Elemento ==")
pilha = Pilha(10)
pilha.Inserir(8)
pilha.Inserir(2)
pilha.Inserir(10)
pilha.Inserir(1)
print("Menor elemento:", pilha.menorElemento())