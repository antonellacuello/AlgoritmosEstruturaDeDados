class Carro :
    def __init__(self) :
        self.placa = None
        self.ano = None
    def __init__(self, placa, ano) :
        self.placa = placa
        self.ano = ano
    def __repr__(self) :
        return 'placa: ' + self.placa + ', ano: ' + str(self.ano)
    def getAno(self) :
        return self.ano
    def getPlaca(self) :
        return self.placa
    def setAno(self, ano) :
        self.ano = ano
    def setPlaca(self, placa) :
        self.placa = placa