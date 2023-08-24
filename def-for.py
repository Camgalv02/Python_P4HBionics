#Mostrar una tabla de multiplicar
"""ejemplo de ciclo for adaptado"""

def tabla_multiplicar(num):
#num=int(input("Escoge un número: ")

    for mult in range (11):
        print(str(num)+"x"+str(mult)+"="+str(num*mult))

tabla_multiplicar(8)
tabla_multiplicar(15)
tabla_multiplicar(9)

        
