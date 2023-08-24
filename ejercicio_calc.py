#CALCULAR LA MEDIA
def calcular_media(*args): #args significa que le vamos a pasar un numero indeterminado de argumentos a nuestra funcion y se van a guardar como una tupla
    total=0
    for i in (args):
        total=total+i
    resultado=total/len(args)
    print("La media es: "+ str(resultado))

    
calcular_media(10,10,10,6)

"""
total=0
total=0+10 =10 //primer valor
total=10+10 =20
total=20+10 =30
total=30+6 =36

divide el resultado entre la cantdidad de valores 36/4=9

"""
