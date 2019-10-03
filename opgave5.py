# En Klasse (på engelsk: class) er det sidste
# vi skal lære om inden vi kan begynde at 
# lave vores eget spil.

# Opgave A:
# Forstå hvad der står herunder.
# Tilføj alder til klassen og udskriv det.

class Person:
	# Funktionen herunder hedder __init__, hvilket er et lidt underligt navn.
	# Det står for "initialize". Funktionen bliver automatisk kaldt, når man skriver:
	# person = Person().
	# Vi kan se at funktionen tager 2 argumenter, self og name.
	# self behøver vi ikke at tænke så meget, det her argument er 
	# automatisk givet til funktionen. Derfor kan vi se at vi kun
	# skal give funktionen et argument: name.

	def __init__(self, name):
		self.hej = name

	def sayMyName(self):
		print("My name is " + self.hej)

print("Opgave A:")

rasmus = Person("Rasmus")
rasmus.skrivA()
rasmus.sayMyName()

# Opgave B:
# Forstå hvad der står her.
# Tilføj ...

print("\nOpgave B:")

class Car: 
	def __init__(self, name, fuel):
		self.name = name
		self.fuel = fuel
		self.km_driven = 0

	# vi kører en kilometer for hver brændstof vi har
	def drive(self, distance):
		self.km_driven += distance
		self.fuel -= distance


car_bmw = Car("BMW", 50)
print("Brændstof:", car_bmw.fuel)
print("Antal kilometer kørt:", car_bmw.km_driven)
car_bmw.drive(20)
print()
print("Brændstof:", car_bmw.fuel)
print("Antal kilometer kørt:", car_bmw.km_driven)

# Svær opgave (du SKAL ikke lave den her):
# 1. Gør sådan så Car klassen kan tage et ekstra argument: Persons
# 	 Dette argument skal være en liste af alle de personer
#	 der er i bilen. For at gøre dette skal du lave en klasse
#	 så vi kan lave personer. Den kan fx tage et navn som input.
#
# 2. Lav en ny funktion i Car klassen der udskriver navnet på alle 
#    personerne i bilen.
# 
# 3. Lav en ny funktion i Car klassen som tilføjer en ny person til 
# 	 bilens liste af personer. Denne funktion tager en Person som input.
