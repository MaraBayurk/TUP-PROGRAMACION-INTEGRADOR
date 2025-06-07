# Árbol de decisiones simple para determinar "qué raza sos" en un mundo de fantasía
arbol = {
    "pregunta": "¿Sos alto?",
    "si": {
        "pregunta": "¿Te apasionan los fuegos artificiales?",
        "si": {"resultado": "Sos un Mago"},
        "no": {"resultado": "Sos un Elfo"}
    },
    "no": {
        "pregunta": "¿Te gusta el oro?",
        "si": {"resultado": "Sos un Enano"},
        "no": {"resultado": "Sos un Hobbit"}
    }
}

#         ------- pregunta -------
#        v                        v
#     rama no                   rama si
#     pregunta                  pregunta

# rama no  rama si          rama no  rama si

# resul   result           result     result


# Estructura del árbol:
# - Raíz: pregunta inicial
# - Ramas: respuestas "si" y "no"
# - Hojas: resultados finales (raza del usuario)

# Función para jugar: recorre el árbol según las respuestas del usuario
# Si llega a un resultado, lo muestra
# Si está en una pregunta, pregunta al usuario y sigue por la rama correspondiente

def jugar(nodo):
    if "resultado" in nodo:
        print(f"Resultado: {nodo['resultado']}")
        return
    respuesta = input(nodo["pregunta"] + " (si/no): ").strip().lower()
    if respuesta == "si":
        jugar(nodo["si"])
    elif respuesta == "no":
        jugar(nodo["no"])
    else:
        print("Respuesta no válida. Por favor respondé 'si' o 'no'.")
        jugar(nodo)

# Función para agregar una nueva pregunta en una hoja del árbol
# camino: lista de pasos ("si"/"no") para llegar a la hoja
# nueva_pregunta: texto de la nueva pregunta
# resultado_si: resultado si la respuesta es "si"
# resultado_no: resultado si la respuesta es "no"
def agregarNodo(arbol, camino, nueva_pregunta, resultado_si, resultado_no):
    nodo = arbol
    for paso in camino:
        if paso in nodo:
            nodo = nodo[paso]
        else:
            print(f"Camino inválido: {paso} no existe")
            return
    if "resultado" not in nodo:
        print("No se puede agregar aquí porque este nodo ya tiene una pregunta.")
        return
    # Reemplazamos el nodo hoja por una nueva pregunta con dos resultados
    nodo.clear()
    nodo["pregunta"] = nueva_pregunta
    nodo["si"] = {"resultado": resultado_si}
    nodo["no"] = {"resultado": resultado_no}
    print(f'Se agregó la pregunta "{nueva_pregunta}" al árbol')
    print(f'El nodo completo: {nodo}')

# Función para buscar el camino desde la raíz hasta una pregunta o resultado
# Devuelve una lista con las preguntas y el resultado si lo encuentra, o None si no existe

def buscarCamino(nodo, destino, camino=None):
    if camino is None:
        camino = []  # Inicializamos el camino si es la primera llamada
    # Si el nodo es una pregunta, la agregamos al camino
    if "pregunta" in nodo:
        camino_actual = camino + [nodo["pregunta"]]
        if nodo["pregunta"] == destino:
            return camino_actual  # Si encontramos la pregunta buscada
        # Buscamos recursivamente en las ramas 'si' y 'no'
        for respuesta in ["si", "no"]:
            if respuesta in nodo:
                resultado = buscarCamino(nodo[respuesta], destino, camino_actual)
                if resultado:
                    return resultado
    # Si el nodo es un resultado (hoja), verificamos si es el destino
    if "resultado" in nodo:
        if nodo["resultado"] == destino:
            return camino + [nodo["resultado"]]  # Devolvemos el camino completo
    # Si no se encontró el destino en este camino
    return None

def calcularPeso(nodo):
    # Si el nodo es un diccionario, seguimos sumando recursivamente
    if type(nodo) is dict:
        cantidad = 1
        for hijo in nodo.values():
            cantidad += calcularPeso(hijo)
        return cantidad
    # Si no, es una hoja (string), cuenta como 1
    return 1

def calcularGrado(nodo):
    # El grado de un nodo es la cantidad de hijos que tiene
    if type(nodo) is dict:
        return len(nodo) - 1  # Restamos 1 porque no contamos la pregunta o resultado
    return 0  # Si es una hoja, no tiene hijos    


# --- Ejemplo de uso ---
# Para jugar, descomentá la línea de abajo:
# jugar(arbol)

# Para agregar una pregunta nueva en la rama "si"->"si":
# print("Árbol actualizado:")
# agregarNodo(
#     arbol,
#     camino=["si", "si"],
#     nueva_pregunta="¿Tenés barba larga?",
#     resultado_si="Sos un Mago",
#     resultado_no="Sos un Hechicero joven"
# )

# # Para buscar el camino hasta un resultado:
# caminoABuscar = buscarCamino(arbol, "¿Te gusta el oro?")
# print(f"Camino encontrado: {caminoABuscar}")

# # Calcular EL PESO DEL ARBOL (la cantidad de nodos en el árbol)
# # PESO: el número total de nodos que tiene el mismo.

peso = calcularPeso(arbol)
print(f"El peso del árbol es igual a {peso}.")

# el grado del arbol es # GRADO DE UN NODO:  número de hijos que tiene dicho nodo

grado = calcularGrado(arbol)
print(f'El grado del árbol es: {grado}')

