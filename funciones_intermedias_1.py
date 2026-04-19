#1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431

#2. Iterar a través de una lista de diccionarios
#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]


def iterarDiccionario(cantantes):
    for cantante in cantantes:
        print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir:


#iterarDiccionario2(“pais”, cantantes) debe de imprimir:
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario[llave])


#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave. Por ejemplo:
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, lista_valores in diccionario.items():
        # Imprime el tamaño de la lista y la clave en mayúsculas
        print(len(lista_valores), clave.upper())
        # Imprime cada elemento de la lista en una línea aparte
        for valor in lista_valores:
            print(valor)

if __name__ == '__main__':
    iterarDiccionario(cantantes)
    iterarDiccionario2("nombre", cantantes)
    iterarDiccionario2("pais", cantantes)
    imprimirInformacion(costa_rica)

