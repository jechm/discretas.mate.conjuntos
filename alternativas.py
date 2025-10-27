#---------------- AÑADIR ELEMENTOS EN UN CONJUNTO DE NOOMBRE X
def añadirElemento(conjunto):
    añadirMas = True
    indice = nombreconjuntos.index(conjunto)  # Obtiene el indice del nombre para saber el indice del sub array donde estaran los elementos de este conjunto
    while añadirMas: # hacer while len(elementos[indice])<10 permite agregar !!!! 
        elemento = input("Ingrese el elemento que quiere agregar ")
        if elemento in elementos[0]:  # ¿Ya existe el elemento en el universo?
            if conjunto == "U":  # Si existe y se quiere agregar Universo
                print("Este elemento ya existe en el conjunto Universo")

            elif (
                elemento in elementos[indice]
            ):  # Si existe y tambien en el nuevo conjunto
                print(f"{elemento} ya existe en {elementos[indice]}")
            elif (
                len(elementos[indice]) > 10
            ):  # existe en el universo pero el conjuto ya tiene 10 elementos
                print(f"el conjunto {conjunto} ya tiene 10 elementos0")
                añadirMas = False
            else:  # el elemento existe en el universo, no en el conjunto indicado y tiene menos de 10 elementos
                elementos[indice].append(elemento)
                print("elemento añadido con exito")
        else:  # El elemento no existe en el universo
            if conjunto == "U":  # se quiere añadir en el conjunto universo
                if len(elementos[0]) < 10:
                    elementos[0].append(elemento)
                    print("Elemento añadido con existo al conjunto Universo")
                else:
                    print("El conjunto universo ya tiene 10 elementos")
                    añadirMas = False

            else:  # El elemento no existe en el universo y el conjunto no es el universo
                print("Este elemento no existe en el conjunto universo")

        if añadirMas == True:
            elemento = input(
                "PRESIONE ENTER PARA AGREGAR MAS, INGRESE N PARA FINALIZAR"
            )
            if elemento == "N":
                añadirMas = False
