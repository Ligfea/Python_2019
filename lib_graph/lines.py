from graph import *

penColor(0, 0, 0)
penSize(1)
point(30, 30) #  рисует точку

penColor(0, 255, 0)
line(120, 60, 60, 30)  # рисует линию

penColor(255, 0 ,0)
moveTo(100, 100)
lineTo(40, 80)
lineTo(140, 70)
lineTo(100, 150)  # рисует ломанную

run()
