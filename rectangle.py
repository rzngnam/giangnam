from turtle import *

speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
mau = 0

for _ in range(5):
    fillcolor(colors[mau])
    pencolor(colors[mau])
    begin_fill()
    for i in range(2):
        forward(50)
        right(90)
        forward(100)
        right(90)
    forward(50)
    mau += 1
    end_fill()

mainloop()