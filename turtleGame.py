import turtle
import random

s = turtle.Screen()
s.title("Tortugas Ninjas")
s.bgcolor("black")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
jugador3 = turtle.Turtle()
jugador4 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("red", "red")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador3.hideturtle()
jugador3.shape("turtle")
jugador3.color("orange", "orange")
jugador3.shapesize(2,2,2)
jugador3.pensize(3)

jugador4.hideturtle()
jugador4.shape("turtle")
jugador4.color("purple", "purple")
jugador4.shapesize(2,2,2)
jugador4.pensize(3)

jugador1.penup()
jugador1.goto(200, 200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250, 240)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250, -170)
jugador2.showturtle()

jugador3.penup()
jugador3.goto(200, 50)
jugador3.pendown()
jugador3.circle(40)

jugador3.penup()
jugador3.goto(-250, 70)
jugador3.showturtle()

jugador4.penup()
jugador4.goto(200, -50)
jugador4.pendown()
jugador4.circle(40)

jugador4.penup()
jugador4.goto(-250, -30)
jugador4.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("Winner RAPHAEL")
        break
    elif jugador2.pos() >= (200, -200):
        print("Winner LEONARDO")
        break
    elif jugador3.pos() >= (200, 50):
        print("Winner MICHELANGELO")

    elif jugador4.pos() >= (200, -50):
        print("Winner DONATELLO")
    else:
        turno1 = input("Presiona ENTER para avanzar a RAPHAEL: ")
        turno1 = random.choice(dado)
        print("Tu número es :",turno1,"\nAvanzas: ",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Presiona para avanzar la tortuga LEONARDO")
        turno2 = random.choice(dado)
        print("Tu número es :",turno2,"\nAvanzas: ",turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)
        
        turno3 = input("Presiona para avanzar la tortuga MICHELANGELO")
        turno3 = random.choice(dado)
        print("Tu número es :",turno3,"\nAvanzas: ",turno3*20)
        jugador3.pendown()
        jugador3.forward(20*turno3)

        turno4 = input("Presiona para avanzar la tortuga MICHELANGELO")
        turno4 = random.choice(dado)
        print("Tu número es :",turno4,"\nAvanzas: ",turno4*20)
        jugador4.pendown()
        jugador4.forward(20*turno4)

turtle.done()