num1 = 20
num2 = 4

print("La suma es:", (num1 + num2))
print("La resta es:", (num1 - num2))
print("La multiplicaciòn es:", (num1 * num2))
print("La divisiòn es:", (num1 / num2))
print("La divisiòn exacta es:", (num1 // num2))
print("La potencia es:", (num1**num2))

# Concatenación en Python

texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
print(textoFinal)

print("El saludo es: %s %s" %(texto1, texto2))

saludoFinal = "Saludo {} {}".format(texto1,texto2)
print(saludoFinal)

saludoFinal2 = "Saludo {y} {x}".format(x=texto1,y=texto2)
print(saludoFinal2)
