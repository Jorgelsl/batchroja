diccionario = {"nombre":"Carlos","edad":22,"cursos":["Python","Flask"]}
print(diccionario)
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["cursos"])

dic = dict(nombre="Nestro",apellido="Juarez",edad=22)
#print(dic["nombre"])
print("__________________________")
for key,value in diccionario.items():
	print(key + " " + str(value))

lista_cursos = diccionario["cursos"]
lista_cursos.append("Java")
print(lista_cursos)
print(diccionario)

print("__________________________")

#Devuelve el numero de elementos que tiene el diccionario.
print(len(diccionario))

#Devuelve una lista con las claves del diccionario.
print(diccionario.keys())

#Devuelve una lista con los calores del diccionario.
print(diccionario.values()) 

#Devuelve el valor del elemento con su clave, Y si no lo encuentra tare un valor por default
print(diccionario.get("nombre","JUANITO"))

#Inserta un elemento al diccionario con su clave:valor
diccionario["key"] = "value"
print(diccionario)

diccionario.pop("key")
print(diccionario)


