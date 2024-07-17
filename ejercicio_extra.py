"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
lista_alumnos=[
    {
        "tienda":"bara",
        "celular":928453777,
    },
     {
        "tienda":"mavelita",
        "celular":928453788,
    },
     {
        "tienda":"baras",
        "celular":928452772,
    },
     {
        "tienda":"nina",
        "celular":928456666,
    },
     {
        "tienda":"luffy",
        "celular":928454444,
    }
]
def objeto(e):
        e["tienda"]="zoro"
        return [e]

lista_actualizada=list(filter(objeto,lista_alumnos))
print(lista_actualizada[1])