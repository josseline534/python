import random


def verificar_numero(numero_aleatorio):
    numero_ingresado = ingresar_numero()
    while numero_ingresado != numero_aleatorio:
        if numero_ingresado > numero_aleatorio:
            print("Es un número más pequeño")
        else:
            print("Es un número más grande")
        numero_ingresado = ingresar_numero()
    print("Ganaste...")


def ingresar_numero():
    return int(input("Escriba un numero del 1 al 100: "))


def run():
    numero_aleatorio = random.randint(1,101)
    comparar = verificar_numero(numero_aleatorio)



if __name__ == '__main__':
    run()