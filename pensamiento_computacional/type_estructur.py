""" Tipos estructurados """

my_tupla = ()
print(type(my_tupla))
""" my_tupla = (1, 'dos', True) """
my_tupla = (0,)
my_other_tuple = (2, 5, 8)
my_tupla += my_other_tuple
x, y, z = my_other_tuple
print(f'TUPLA: {my_tupla}')
print(f'X: {x}')
print(f'Y: {y}')
print(f'Z: {z}')


def cordenadas():
    return (4, 8)


cordenada = cordenadas()
a, b = cordenada
print(f'A: {a}')
print(f'B: {b}')
