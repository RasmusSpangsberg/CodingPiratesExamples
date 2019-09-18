# Funktioner er noget vi kan bruge til at 
# give et navn til et lille stykke kode,
# som vi så kan bruge igen. Hvis du nogensinde
# har copy-pastet noget kode, skulle du nok 
# have brugt en funktion i stedet.

# Opgave A - Kan du finde de steder der er 
# blevet copy-pastet? Skriv dem som en funktion
# i stedet.
# Hint:

# Her har vi lavet en funktion der 
# printer noget når den bliver kaldt.
def hej():
	print("Hej med dig")

# her kalder vi funktionen
hej()


import turtle

t = turtle.Turtle()
t.penup()
t.goto(-250, 0)
t.pendown()

for i in range(8):
	t.forward(40)
	t.left(45)

t.penup()
t.right(45)
t.forward(100)
t.pendown()

for i in range(8):
	t.forward(40)
	t.left(45)

t.penup()
t.left(90)
t.forward(200)
t.pendown()

for i in range(8):
	t.forward(40)
	t.left(45)

turtle.done()