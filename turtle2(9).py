#Artur Snigurski
#IT20

import turtle

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Hindeline töö - Artur Snigurski")

t1 = turtle.Turtle()
t1.speed(0)

for x in range(0,4):
    t1.fd(20)
    t1.lt(90)
    t1.fd(20)
    t1.rt(90)
    t1.fd(20)
    t1.rt(90)

t2 = turtle.Turtle()
t2.speed(0)

for x in range(0,4):
   t2.lt(90)
   t2.fd(20)
   t2.lt(90)
   t2.fd(20)
   t2.rt(90)
   t2.fd(20)
   
t3 = turtle.Turtle()
t3.speed(0)

for x in range(0,4):
    t3.fd(20)
    t3.lt(90)
    t3.fd(20)
    t3.rt(90)
    t3.fd(20)
    t3.lt(90)
   
t4 = turtle.Turtle()
t4.speed(0)


for x in range(0,4):
    t4.rt(90)
    t4.fd(20)
    t4.lt(90)
    t4.fd(20)
    t4.rt(90)
    t4.fd(20)