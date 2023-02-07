"""Найти сумму чисел списка стоящих на нечетной позиции"""


from random import randint as rand
data = [rand(5,25) for i in range(10)]
print(data)
print(sum(data[1::2]))
