my_dict = {
    'David': 35,
    'Ericka': 32,
    'Jaime': 50
}
print(my_dict['David'])
print(my_dict.get('Juan', 30))
print(my_dict.get('Jaime', 30))
my_dict['Jaime'] = 20
print(my_dict)
my_dict['Pedro'] = 70
print(my_dict)
del my_dict['Jaime']
print(my_dict)
for llave in my_dict.keys():
    print(llave)
for valor in my_dict.values():
    print(valor)
for llave, valor in my_dict.items():
    print(llave, valor)
print('David' in my_dict)
print('Tom' in my_dict)
