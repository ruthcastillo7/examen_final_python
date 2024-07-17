"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
lista_alumnos=[
    {
        "nombre":"ruth",
        "apellido":"castillo",
        "edad":18,
        "celular":928453777,
        "email":"castillohuamaniruthm@gmail.com"
    },
     {
        "nombre":"flor",
        "apellido":"lucana",
        "edad":18,
        "celular":928453777,
        "email":"florlucana@gmail.com"
    }
]

print(lista_alumnos)

def objeto(e):
        e["nombre"]="luffy"
        return [e]

lista_actualizada=list(filter(objeto,lista_alumnos))
print(lista_actualizada[1])