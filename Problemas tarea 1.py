'''
palabras = int (input("Cuantas palabras tiene la lista"))

lista = []
if palabras < 0:
	print("No jodas chato")
else:
	for i in range (1, palabras + 1):
		palabra1 = (input("Pon los nombres chato " + str (i)))
		lista.append(palabra1)
	print(lista) 
'''
'''
palabras = int (input("Cuantas palabras tiene la lista "))

lista = []
if palabras < 0:
	print("No jodas chato")
else:
	for i in range (1, palabras + 1):
		palabra1 = (input("Pon los nombres chato " + str (i)))
		lista.append(palabra1)
	print(lista) 

palabras2 = input("¿Qué palabra quieres buscar?\n ")

var1 = lista.count(palabras2)
print("La palabra " + str (palabras2) + " aparece " + str(var1) + " veces en la lista chavo.")

palabras3 = input("¿Qué palabra quieres cambiar (aunque no sea cierto) \n ")
palabras4 = input("¿Qué palabra quieres agregar (aunque no sea cierto) \n ")
var2 = lista.index(palabras3)
lista[var2] = palabras4

print(lista)
'''

palabras = int (input("Cuantas palabras tiene la lista "))

lista = []
if palabras < 0:
	print("No jodas chato")
else:
	for i in range (1, palabras + 1):
		palabra1 = (input("Pon los nombres chato " + str (i) + " "))
		lista.append(palabra1)
	print(lista) 

palabras2 = input("¿Qué palabra quieres buscar?\n  ")

var1 = lista.count(palabras2)
print("La palabra " + str (palabras2) + " aparece " + str(var1) + " veces en la lista chavo.")

palabras3 = input("¿Qué palabra quieres quitar (aunque no sea cierto) \n ")
for i in lista:
	if i == palabras3:
		lista.remove(palabras3)
print(lista)		

 


