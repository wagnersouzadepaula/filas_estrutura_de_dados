from Veiculo import Veiculo


class Drone(Veiculo):
    def __init__(self, marca=None, modelo=None, qtdHelices=None):
        super().__init__(marca, modelo)
        self._qtdHelices = qtdHelices

    @property
    def gsmarca(self):
        return self.marca

    @gsmarca.setter
    def gsmarca(self, marca):
        self.marca = marca

    @property
    def gsmodelo(self):
        return self.modelo

    @gsmodelo.setter
    def gsmodelo(self, modelo):
        self.modelo = modelo

    @property
    def gsqtdHelices(self):
        return self._qtdHelices

    @gsqtdHelices.setter
    def gsqtdHelices(self, qtdHelices):
        self._qtdHelices = qtdHelices

    @property
    def getInformacoes(self):
        print(f"""
        MARCA: {self.marca}
        MODELO: {self.modelo}
        QTD DE HÉLICES: {self._qtdHelices}
        """)

    def cadastrar(self, marca, modelo, qtdHelices):
        self.marca = marca
        self.modelo = modelo
        self._qtdHelices = qtdHelices
