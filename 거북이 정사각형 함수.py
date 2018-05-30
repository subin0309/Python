import turtle
t=turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
length=int(input("변의 길이를 입력하시오: "))
t.up()
t.goto(-200,0)
t.down()
square(length);

length=int(input("변의 길이를 입력하시오: "))
t.up()
t.goto(0,0)
t.down()
square(length);

length=int(input("변의 길이를 입력하시오: "))
t.up()
t.goto(200,0)
t.down()
square(length);
