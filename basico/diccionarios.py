def run():
    mi_diccionario={
        'llave1':1,
        'llave2':2,
        'llave3':3
    }
    población_paises = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }
    print(población_paises)

    for pais in población_paises.keys():
        print(pais)
        print(población_paises[pais])

    for pais in población_paises.values():
        print(pais)

    for pais, poblacion in población_paises.items():
        print("El país "+ pais + " tiene " + str(poblacion) +" habitantes.")


if __name__ == '__main__':
    run()