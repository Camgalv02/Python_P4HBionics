#ejemplo de variables locales y globales
def ejemplo():
    a=5 """esta es una variable local"""
    suma= a+a
    print (suma)
    return

a=3 """esta es una variable global"""
ejemplo()
print (a)
