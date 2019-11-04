from graph import *


def triangle(x, y, z):  # создание функции, которая генерирует треугольник, согласно x, y и z,
    # где x и y отвечают за координаты, а z за цвет заливки треугольника.
    brushColor(z)
    polygon([(x, y), (x, y - 60),
             (x + 100, y), (x, y)])


penColor("black")
triangle(100, 100, "blue")
triangle(200, 100, "red")
triangle(200, 160, "green")

run()
