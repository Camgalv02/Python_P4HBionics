#Mostrar tabla de multiplicar

num= int (input("Escoge un número: "))

"""
esta linea: for mult in [1,2,3,4,5,6,7,8,9,10]: se puede reemplazar con la funcion RANGE que cumple la misma funcion pero restandole un numero
a la iteracion que le coloquemos, es decir que si le ponemos el valor 9, nos va a mostrar 9 filas ya que arranca del cero si quisieramos que
nos muestre la tabla completa de multiplicar tendriamos que ponerle 11.
en otras palabras, el valor que necesitamos +1.
"""

for mult in range(11):

"""
tambien se pueden utilizar intervalos: es decir
                                                    for mult in range(1, 11, 2):
que nos va a mostrar de 2 en dos los valores de la tabla que ingresemos
"""
    
    print (str(num) + "x" + str(mult) + "=" + str(num*mult))
           
        #el numero que eligio el usuario x el numero por el que se va a
        #igual a la operacion multiplicar

        #y convertimos las variables num y mult que estan en valor int a string colocando str y la variable entre parentesis
