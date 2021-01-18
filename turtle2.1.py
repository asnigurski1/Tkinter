#Artur Snigurski
#IT20

import turtle

aken = turtle.Screen()
aken.setup(1200,500)
aken.title("Hindeline töö - Artur Snigurski")


#Esimene maja
keha = turtle.Turtle()
keha.speed(0)

for x in range(0,2):
    keha.fd(30)
    keha.lt(90)
    keha.fd(35)
    keha.lt(90)

uks = turtle.Turtle()
uks.speed(0)

uks.color('blue')
uks.penup()
uks.fd(7)
uks.pendown()
uks.lt(90)
uks.fd(20)
uks.rt(90)
uks.fd(16)
uks.rt(90)
uks.fd(20)

katus = turtle.Turtle()
katus.speed(0)

katus.color('green')
katus.penup()
katus.lt(90)
katus.fd(35)
katus.pendown()
katus.rt(30)
katus.fd(30)
katus.rt(120)
katus.fd(30)


#Teine maja
keha2 = turtle.Turtle()
keha2.speed(0)

keha2.penup()
keha2.fd(45)
keha2.pendown()


for x in range(0,2):
    keha2.fd(45)
    keha2.lt(90)
    keha2.fd(52)
    keha2.lt(90)
    
uks2 = turtle.Turtle()
uks2.speed(0)

uks2.penup()
uks2.fd(45)
uks2.pendown()
uks2.color('blue')
uks2.penup()
uks2.fd(10)
uks2.pendown()
uks2.lt(90)
uks2.fd(30)
uks2.rt(90)
uks2.fd(24)
uks2.rt(90)
uks2.fd(30)

katus2 = turtle.Turtle()
katus2.speed(0)

katus2.penup()
katus2.fd(45)
katus2.pendown()

katus2.color('green')
katus2.penup()
katus2.lt(90)
katus2.fd(52)
katus2.pendown()
katus2.rt(30)
katus2.fd(45)
katus2.rt(120)
katus2.fd(45)


#Kolmas maja
keha3 = turtle.Turtle()
keha3.speed(0)

keha3.penup()
keha3.fd(105)
keha3.pendown()


for x in range(0,2):
    keha3.fd(60)
    keha3.lt(90)
    keha3.fd(70)
    keha3.lt(90)
    
uks3 = turtle.Turtle()
uks3.speed(0)

uks3.penup()
uks3.fd(90)
uks3.pendown()
uks3.color('blue')
uks3.penup()
uks3.fd(29)
uks3.pendown()
uks3.lt(90)
uks3.fd(40)
uks3.rt(90)
uks3.fd(32)
uks3.rt(90)
uks3.fd(40)


katus3 = turtle.Turtle()
katus3.speed(0)

katus3.penup()
katus3.fd(105)
katus3.pendown()

katus3.color('green')
katus3.penup()
katus3.lt(90)
katus3.fd(70)
katus3.pendown()
katus3.rt(30)
katus3.fd(60)
katus3.rt(120)
katus3.fd(60)

#Neljas maja
keha4 = turtle.Turtle()

keha4.speed(0)
keha4.penup()
keha4.fd(180)
keha4.pendown()


for x in range(0,2):
    keha4.fd(45)
    keha4.lt(90)
    keha4.fd(52)
    keha4.lt(90)
    
uks4 = turtle.Turtle()
uks4.speed(0)

uks4.penup()
uks4.fd(180)
uks4.pendown()
uks4.color('blue')
uks4.penup()
uks4.fd(10)
uks4.pendown()
uks4.lt(90)
uks4.fd(30)
uks4.rt(90)
uks4.fd(24)
uks4.rt(90)
uks4.fd(30)

katus4 = turtle.Turtle()
katus4.speed(0)

katus4.penup()
katus4.fd(180)
katus4.pendown()

katus4.color('green')
katus4.penup()
katus4.lt(90)
katus4.fd(52)
katus4.pendown()
katus4.rt(30)
katus4.fd(45)
katus4.rt(120)
katus4.fd(45)

#Viies maja
keha5 = turtle.Turtle()
keha5.speed(0)

keha5.penup()
keha5.fd(240)
keha5.pendown()

for x in range(0,2):
    keha5.fd(30)
    keha5.lt(90)
    keha5.fd(35)
    keha5.lt(90)

uks5 = turtle.Turtle()
uks5.speed(0)

uks5.penup()
uks5.fd(240)
uks5.pendown()
uks5.color('blue')
uks5.penup()
uks5.fd(7)
uks5.pendown()
uks5.lt(90)
uks5.fd(20)
uks5.rt(90)
uks5.fd(16)
uks5.rt(90)
uks5.fd(20)

katus5 = turtle.Turtle()
katus5.speed(0)

katus5.penup()
katus5.fd(240)
katus5.pendown()
katus5.color('green')
katus5.penup()
katus5.lt(90)
katus5.fd(35)
katus5.pendown()
katus5.rt(30)
katus5.fd(30)
katus5.rt(120)
katus5.fd(30)


#Kuues maja
keha6 = turtle.Turtle()
keha6.speed(0)

keha6.penup()
keha6.fd(285)
keha6.pendown()


for x in range(0,2):
    keha6.fd(45)
    keha6.lt(90)
    keha6.fd(52)
    keha6.lt(90)
    
uks6 = turtle.Turtle()
uks6.speed(0)

uks6.penup()
uks6.fd(285)
uks6.pendown()
uks6.color('blue')
uks6.penup()
uks6.fd(10)
uks6.pendown()
uks6.lt(90)
uks6.fd(30)
uks6.rt(90)
uks6.fd(24)
uks6.rt(90)
uks6.fd(30)

katus6 = turtle.Turtle()
katus6.speed(0)

katus6.penup()
katus6.fd(285)
katus6.pendown()

katus6.color('green')
katus6.penup()
katus6.lt(90)
katus6.fd(52)
katus6.pendown()
katus6.rt(30)
katus6.fd(45)
katus6.rt(120)
katus6.fd(45)
