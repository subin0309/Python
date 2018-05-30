import turtle
t=turtle.Turtle()
t.shape("turtle")

def shape(n):
    for i in range(n):
        t.forward(100)
        t.left(360/n)

n=int(input("몇각형을 만들까욤?:"))
shape(n)
n=int(input("몇각형?"))
shape(n)
n=int(input("몇각형?"))
shape(n)
