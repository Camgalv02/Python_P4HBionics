"""
Ejercicio 5
Escribir un programa que solicite una contraseña (el texto de la
contraseña no es importante) y la vuelva a solicitar hasta que las
dos contraseñas coincidan.
"""

contra1= str(input("Introduzca su contraseña: "))
contra2= str(input("Repita su contraseña: "))

while (contra1 != contra2):
    print ("Intente de nuevo")
    contra1= str(input("Introduzca su contraseña: "))
    contra2= str(input("Repita su contraseña: "))
print ("Contraseña Correcta, Bienvenido")    
