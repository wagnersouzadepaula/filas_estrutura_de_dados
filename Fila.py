from No import No


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("A Fila está vazia!")
        else:
            print("----------------------------")
            aux = self.inicio
            while aux:
                if aux.dado.getInformacoes is not None:
                    print(aux.dado.getInformacoes)
                aux = aux.proximo
            print(f"Tamanho da lista: {self.tamanho}")

    def remover(self):
        if self.inicio is None:
            print("Fila Vazia!")
        else:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None
                self.tamanho = 0
            else:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            self.imprimir()
