print("Lectura de numeros")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2 :
    print(f"El {num1} es mayor que el {num2}")
else:
    print(f"El {num2} es mayor que el {num1}")
    
print("-------------- PEDIR UNA EDAD ------------------------")

edad = int(input("Ingresa su edad"))

if edad > 18 :
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18")
else:
    print("No eres mayor de edad")