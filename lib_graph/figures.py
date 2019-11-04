from graph import *

penColor("cyan")
brushColor("yellow")
rectangle(10, 20, 50, 40)  # рисует прямоугольник (первые 2 коородинаты - первая точка,
# последние 2 координаты - вторая точка)

penColor("magenta")
brushColor("green")
polygon([(60, 60), (100, 100),
         (60, 100), (60, 60)])
# команда может сделать любую фигуру с углами.
# в данном случае она рисует треугольник - первая и последняя координаты совпадают,
# что отправляет кисть в начало,
# образовывая треугольник


penColor(255, 255, 0)
brushColor(255, 0, 255)
circle(150, 40, 30)  # рисует окружность (пераве 2 цифры - ккорды точки-центра окружности, 3я - радиус этой окр)

run()
