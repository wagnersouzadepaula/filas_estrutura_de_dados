from abc import ABCMeta, abstractmethod


class Veiculo(metaclass=ABCMeta):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @property
    def gsmarca(self):
        pass

    @gsmarca.setter
    @abstractmethod
    def gsmarca(self, marca):
        pass

    @property
    def gsmodelo(self):
        pass

    @gsmodelo.setter
    @abstractmethod
    def gsmodelo(self, modelo):
        pass

    @property
    def getInformacoes(self):
        print(f"""
        NOME: {self.marca}
        MODELO: {self.modelo}
        """)

    @abstractmethod
    def cadastrar(self, marca, modelo):
        pass
