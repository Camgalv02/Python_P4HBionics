#Mostrar tabla de multiplicar

num= int (input("Escoge un número: "))

#mostrar una tabla del uno al 10

for mult in [1,2,3,4,5,6,7,8,9,10]:
    print (str(num) + "x" + str(mult) + "=" + str(num*mult))
           
        #el numero que eligio el usuario x el numero por el que se va a
        #igual a la operacion multiplicar

        #y convertimos las variables num y mult que estan en valor int a string colocando str y la variable entre parentesis
