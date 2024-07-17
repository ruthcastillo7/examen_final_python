"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""

lista={3,6,5,7,8,4,1}

def lista_num(lista:list):
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor
def lista_num(lista:list):
    menor=lista[0]
    for x in lista:
        if x < menor:
            menor=x
    return menor
print(f"{lista}")