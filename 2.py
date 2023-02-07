"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21 """
from math import sqrt
doc1 = list(map(int, input("Введите координаты А: ").split()))
doc2 = list(map(int, input("Введите координаты В: ").split()))
def dist(x,y):
    return sqrt(sum(map(lambda p: (p[0]-p[1])**2,zip(x,y))))
print(f"Расстояние между точками А {doc1} и В {doc2} в 2D пространстве равно -> "+"{0:.3f}".format(dist(doc1,doc2)))
