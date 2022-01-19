""" range(comienzo, fin, pasos) """
my_range = range(1, 5)
my_other_range = range(0, 7, 2)
other_range = range(0, 8, 2)
print(my_other_range == other_range)
for i in my_other_range:
    print(i)
print(my_other_range is other_range)
for i in other_range:
    print(i)

my_range_par = range(1, 100, 2)
print(my_range_par)

for i in my_range_par:
    print(i)
