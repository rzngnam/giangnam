from turtle import *

speed(0)
socanh = 3
mau = -2
color = ["blue","red"]
for _ in range(4):
    pencolor(color[mau])
    for _ in range(socanh):
        forward(80)
        left(360/socanh)
    socanh += 1
    mau += 1

mainloop()