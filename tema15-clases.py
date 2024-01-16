import os

class OperasBas:
    #Declaración de propiedades
    num1 = 0
    num2 = 0
    res = 0
    
    # Declaración de constructor
    def __init__(self, a, b) :
        self.num1 = a
        self.num2 = b
        
    # Declaración de metodos de clase
    def suma(self):
        self.res = self.num1 + self.num2
        print(f"La suma es: {self.res}")
        
def main():
    #Linea para limpiar la terminal
    os.system('cls')
    obj = OperasBas(3,4)
    obj.suma()
    
if __name__ == "__main__":
    main()