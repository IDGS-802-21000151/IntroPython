miDiccionario = {
    "matricula": 1234,
    "nombre": "Jesús",
    "apellidos": "Luvian Luis"
}

print(miDiccionario)
print(miDiccionario["matricula"])
print(miDiccionario["nombre"])
print(miDiccionario["apellidos"])
print(type(miDiccionario))

miDiccionario["nombre"] = "Eduardo"
print(miDiccionario)

miDiccionario["correo"] = "jesus@gmail.com"
print(miDiccionario)