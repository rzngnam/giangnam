from turtle import *

speed(0)

n = 3
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
mau = 0
for _ in range(5):
    for _ in range(n):
        pencolor(colors[mau])
        forward(80)
        left(360/n)
    n += 1
    mau += 1

mainloop()