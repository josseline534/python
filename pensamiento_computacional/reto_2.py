def addUser():
    user = dict(nombre=input('Ingrese su nombre: '),
                edad=int(input('Ingrese su edad: ')))
    return user


def run():
    users = []
    for n in range(2):
        users.append(addUser())
    if users[0]['edad'] > users[1]['edad']:
        print(
            f'El usuario {users[0]["nombre"]} es mayor que el usuario {users[1]["nombre"]}')
    elif users[0]['edad'] < users[1]['edad']:
        print(
            f'El usuario {users[1]["nombre"]} es mayor que el usuario {users[0]["nombre"]}')
    else:
        print(
            f'El usuario {users[0]["nombre"]} tiene la misma edad que el usuario {users[1]["nombre"]}')


if __name__ == '__main__':
    run()
