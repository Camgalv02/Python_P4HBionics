"""Ejercicio 2
Como jefe de programacion en la empresa P4HBionics, estas buscando un nuevo miembro para ampliar el equipo. 
Debe ser un persona de edad entre 18 y 60 anios y que tenga experiencia previa programando en python. 
"1" indica que si tienen experiencia previa, y "0" indica que no tienen experiencia previa.
Escribe un programa que comprueba la edad del candidato y si tienen experiencia previa en python.
El programa debera mostrar "Eligible" si el candidato cumple los requerimientos, y "No Eligible" sino los cumple
"""

edad= int (input("Introduzca la edad: "))
if(edad >=18) & (edad<=60):
    exp= int (input("Tiene experiencia programando en Python?: SI=1/ NO=0 "))
    if (exp==1):
        print ("Es Elegible")
    else:
            print("No Elegible")

elif (edad>60):print("Sobrepasa la edad para el puesto")
else:
    print("Es menor de edad")
    
              
