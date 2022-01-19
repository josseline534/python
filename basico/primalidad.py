def validar_primo(numero):
    for n in range(1,numero+1):
        if n == 1 or n == numero or n == 0:
            continue
        if numero % n == 0:
            return False
    return True


def run():
    numero = int(input("Ingrese un número: "))
    validar = validar_primo(numero)
    if validar:
        print("El número "+ str(numero) +" es primo.")
    else:
        print("El número "+ str(numero) +" no es primo.")


if __name__ == '__main__':
    run()