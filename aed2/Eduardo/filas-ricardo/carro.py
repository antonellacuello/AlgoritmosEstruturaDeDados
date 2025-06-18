class Carro:
    def __init__(self):
        self.placa = None
        self.ano = None
    def __init__(self, placa, ano):
        self.placa = placa
        self.ano = ano
    def __repr__(self):
        return 'Carro("' + str(self.placa) + '",' + str(self.ano) + ')'
        # código que reproduz o objeto
    def __str__(self):
        return "Placa:" + self.placa + "Ano:" + str(self.ano)
        #saída para o usuário da aplicação
    def getAno(self):
        return self.ano
    def getPlaca(self):
        return self.placa
    def setAno(self, ano):
        self.ano = ano
    def setPlaca(self, placa):
        self.placa = placa

#var = Carro("IXH7999", 2017)
#print (var)
#print (repr(var))