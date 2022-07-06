from Carro import Carro
from Drone import Drone
from Fila import Fila


def imprimeMenu():
    print("""
    Escolha conforme o menu abaixo:
    MENU
    1 - Cadastrar Carro na fila
    2 - Remover Carro da fila
    3 - Imprime fila de Carros
    4 - Cadastrar Drone na fila
    5 - Remover Drone da fila
    6 - Imprime fila de Drones
    qualquer outro número - Sair
    """)


listaCarro = Fila()
listaDrones = Fila()

########
# MAIN #
########

continua = True
while continua:
    imprimeMenu()
    escolha = int(input("Faça sua escolha: "))
    if escolha == 1:
        marca = input("Informe a MARCA do CARRO: ")
        modelo = input("Informe o MODELO do CARRO: ")
        qtdPortas = input("Informe a QTDE DE PORTAS do CARRO: ")
        carro = Carro()
        carro.cadastrar(marca, modelo, qtdPortas)
        listaCarro.adicionar(carro)
    elif escolha == 2:
        listaCarro.remover()
    elif escolha == 3:
        listaCarro.imprimir()
        input("FIM DA IMPRESSÃO! [PRESSIONE ENTER]")
    elif escolha == 4:
        marca = input("Informe a MARCA do DRONE: ")
        modelo = input("Informe o MODELO do DRONE: ")
        qtdHelices = input("Informe a QTDE DE HÉLICES do DRONE: ")
        drone = Drone()
        drone.cadastrar(marca, modelo, qtdHelices)
        listaDrones.adicionar(drone)
    elif escolha == 5:
        listaDrones.remover()
    elif escolha == 6:
        listaDrones.imprimir()
        input("FIM DA IMPRESSÃO! [PRESSIONE ENTER]")
    else:
        print("Fim do Programa!!!")
        break
