#for i in range(1, 11):
    #print(f"Tabla del {i}")
    
    #for k in range(1, 11):
        #print(f"{i} x {k} = {i*k}")
        
nombres = ["Mario", "Juan", "Dario", "Pedro"]

for nombre in nombres:
    print(nombre)
    
for index, nombre in enumerate(nombres):
    print("Índice:", index)
    print("Nombre:", nombre)