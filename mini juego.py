"""
#Mecanismo del juego:
#El juego pedirá que introduzcamos un número
#El programa te dirá si el número a adivinar es mayor o menor que el número introducido
#El juego te dará tres oportunidades para adivinar.
#Cuando se acaben los intentos, el juego mostrará "GAME OVER"
#En caso que adivines el número, el juego mostrara "WINNER"

#Pasos a seguir
Elegir un número, entre un rango del 1 al 10
Crear una función llamada juego
  Crear una variable para guardar el número de intentos
  Pedir un número al usuario con input
  Bucle que finaliza cuando se introduce el número ganador o se acaban los intentos.
  En cada paso del bucle, evaluar si el numero secreto es mayor que el número introducido
  y el juego mostrará "el número secreto es mayor" y si no mostrará "el número secreto es menor"
  El juego pedirá de nuevo otro número al usuario e incrementará el número de intentos
Crear una función Resultados
  Si el número de intentos es menor al número máximo de intentos
  significa que el usuario adivinó y mostrará el msj de ganador
  sino el número máximo ha sido alcanzado y mostrará el msj de juego terminado.

#Para generar un número aleatorio, primero declarar la librería random
y utilizar la siguiente función:
random.randint(a, b)
Retorna un entero aleatorio N tal que a <= N <= b. 
"""

#Minijuego para adivinar un número
def juego(numero_secreto, intentos): #crear función juego con 2 argumentos
    numero_intentos=1                #variable para guardar el número de intentos
    numero_usuario= int(input("Por favor introduce un número del 1 al 10: ")) #pedir un número al usuario
    #empieza el ciclo while: si número secreto es distinto del número de usuario y si el número de intentos es menor a los intentos máximos, comenzar el bucle
    while (numero_secreto != numero_usuario) and (numero_intentos < intentos): 
        if(numero_secreto> numero_usuario): #En cada repetición, evaluar si el número secreto es mayor o menor al del usuario
            print("El número secreto es mayor")
        else:
            print("El número secreto es menor")
        numero_usuario=int(input("Por favor vuelve a introducir un número: ")) #Pedir de nuevo al usuario un número
        numero_intentos= numero_intentos + 1 #aumentar el número de intentos en 1
    return numero_intentos #valor que retorna nuestra función juego
def resultados(numero_intentos, intentos): #crear una función para imprimir los resultados con dos argumentos
    if(numero_intentos <= intentos): #si el número de intentos es menor o igual al num max de intentos
        print("*********")
        print("WINNER")  #imprimir Winner
        print("*********")
    else:
        print("*********")
        print("GAME OVER") #si no imprimir Game over
        print("*********")

import random #importar esta libreria para utilizar un numero aleatorio
numero_secreto = random.randint(1,10) #generar un número aleatorio y guardarlo en numero_secreto
intentos= 3 #num max de intentos
numero_intentos = juego(numero_secreto, intentos) #guardar el valor que retorna "juego" en numero_intentos
resultados(numero_intentos, intentos) #llamar a la función resultados para mostrar los mensajes.
