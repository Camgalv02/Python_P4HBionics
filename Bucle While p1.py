#Mostrar tabla de multiplicar con bucle while

num= int (input("Escoge un número: "))
mult=0


while(mult<11):
    print (str(num) + "x" + str(mult) + "=" + str(num*mult))
    mult=mult+1
print ("tabla terminada")
    
