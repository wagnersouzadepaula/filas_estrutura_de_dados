from Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca=None, modelo=None, portas=None):
        super().__init__(marca, modelo)
        self.__portas = portas

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
    def gsportas(self):
        return self.__portas

    @gsportas.setter
    def gsportas(self, portas):
        self.__portas = portas

    @property
    def getInformacoes(self):
        print(f"""
        MARCA: {self.marca}
        MODELO: {self.modelo}
        PORTAS: {self.__portas}
        """)

    def cadastrar(self, marca, modelo, portas):
        self.marca = marca
        self.modelo = modelo
        self.__portas = portas
