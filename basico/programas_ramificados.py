def run():
    num_1 = int(input(' Ingrese un número entero: '))
    num_2 = int(input(' Ingrese un número entero: '))
    if num_1 > num_2:
        print(f'El {num_1} es mayor que {num_2}')
    elif num_2 > num_1:
        print(f'El {num_2} es mayor que {num_1}')
    else:
        print(f'El {num_1} es igual a {num_2}')


if __name__ == '__main__':
    run()
