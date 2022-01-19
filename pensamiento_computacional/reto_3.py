def enumeracion_exhaustiva():
    objetivo = int(input('Ingresa un numero entero: '))
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadra exacta.')


def búsqueda_binaria():
    objetivo = int(input('Ingresa un número entero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo)/2
    print(f'La raiz cuadrada del {objetivo} es: {respuesta}')


def aproximacion():
    objetivo = int(input('Ingresa un numero entero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta)
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta ** -objetivo) >= epsilon:
        print(f'No se encontro raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def error():
    print('error')


def menu():
    print('----MENU----\n1. Enumeración exahustiva\n2. Búsqueda binaria\n3. Aproximación')
    return int(input('Indique el método para calcular raíz cuadra: '))


def metodo(num):
    switch = {
        1: enumeracion_exhaustiva,
        2: búsqueda_binaria,
        3: aproximacion,
    }
    switch.get(num, error)()


def run():
    num = 0
    while(num <= 0 or num > 4):
        num = menu()
    metodo(num)


if __name__ == '__main__':
    run()
