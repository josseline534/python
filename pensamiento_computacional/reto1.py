def run():
    nombre = input('¿Cual es tu nombre? ')
    saludo = f'Hola {nombre}, bienvenido...'
    print(saludo)
    print(f'La longitud del saludo es: {len(saludo)}')


if __name__ == '__main__':
    run()
