num1 = 30
num2 = 0

try:
    resultado = num1/num2
except Exception as e:
    print("Error en el programa -----------------------------")
    print(f'Tipo de excepción: {e}')
finally:
    print("Yo siempre aparezco")