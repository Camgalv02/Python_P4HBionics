"""
Ejercicio 1
Escribir un programa en el que introduzcas el numero representando del 1 al 7 
representando el dia de la semana, y te devuelva el nombre del dia de la semana
ejemplo:
Entrada=1 Salida= Lunes
Entrada=4 Salida= Jueves
"""

num=int(input("Ingrese un número del 1 al 7: "))


if(num==1): print("Lunes")
elif (num==2): print("Martes")
elif (num==3):print("Miercoles")
elif (num==4): print("Jueves")
elif (num==5):print("Viernes")
elif (num==6): print("Sabado")
elif(num==7): print("Domingo")
else: print("Programa Finalizado")
