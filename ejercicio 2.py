x = int(input("Ingresa un numero X \n"))
y = int(input("Ingresa un numero Y \n"))

z = x % y

print(z)

if z == 0:
	print("Exacta")
else:
	print("No")


a = int(input("Ingresa un numero X \n"))
b = int(input("Ingresa un numero Y \n"))



if a > b:
	print("El primero es el numero mayo")
elif b > a:
	print("El primero es el numero menor")	
elif a == b:
	print ("El valor es el mismo")



e = int(input("Ingresa el año actual\n"))
f = int(input("Ingresa el año que prefieras \n"))

if e > f:
	print("Faltan " + str(e - f))
else:
	print("Ya pasaron " + str(f - e)) 	





h = int(input("Ingresa un numero porfis\n"))
i = int(input("Ingresa otro numero \n"))
j = int(input("El ultimo y nos vamos\n"))


if h > i and i > j:
	print("el numero mayoes es " + str(h))
elif i > h and h > j:
	print("el numero mayor es " + str(i))
elif j > h and h > i:
	print("el numero mayor es " + str(j))	


h = int(input("Ingresa un numero\n"))
i = int(input("Ingresa un numero\n"))
j = int(input("Ingresa un numero\n"))

if h == i and  i == j:
	print(("todos son iguales"))
elif h == i and i != j:
	print("el diferente es " + str(j))
elif j == i and i != h:
	print("la obeja negra es " + str(h))	
elif h == j and j != i:
	print("la obeja negra es " + str(i))	


