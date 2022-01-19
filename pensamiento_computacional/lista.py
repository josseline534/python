my_list = [1, 5, 'o']
print(my_list[2])
print(my_list[1:])
my_list.append('Joss')
print(my_list)
my_list[0] = 'Mia'
print(my_list)
my_list.pop()
print(my_list)
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
c = [a, b]
print(c)
a.append(5)
print(a, b, c)

""" Clonar listas """
num = [1, 2, 3]
b = num
c = list(a)
d = num[::]
print(id(num))
print(id(b))
print(id(c))
print(id(d))

""" listas comprehension """
mi_lista = list(range(100))
print(mi_lista)
double_list = [i*2 for i in mi_lista]
print(double_list)
pares_list = [i for i in mi_lista if i % 2 == 0]
print(pares_list)
