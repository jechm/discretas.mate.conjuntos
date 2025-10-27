import os


def limpiar_consola():
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para macOS y Linux
    else:
        os.system("clear")


nombreconjuntos = ["U"]
elementos = [[]]
maxConjuntos = 0


def crearConjunto(nombre):
    if nombre in nombreconjuntos:
        print(f"El conjunto {nombre} ya existe intente de nuevo")
        return False
    else:
        nombreconjuntos.append(nombre)
        elementos.append([])
        print(f"El conjunto {nombre}, ha sido creado con exito")
        return True


def añadirElemento(conjunto):
    añadirMas = True
    indice = nombreconjuntos.index(
        conjunto
    )  # Obtiene el indice del nombre para saber el indice del sub array donde estaran los elementos de este conjunto
    while añadirMas:  # hacer while len(elementos[indice])<10 permite agregar !!!!

        if (
            len(elementos[indice]) < 10
        ):  # Se ejecutara siempre y cuando el conjunto pasado tenga menos de 10 elementos

            elemento = input(
                "Ingrese el elemento que quiere agregar, Dejar Vacio para no añadir mas: "
            )
            if elemento != "":
                if elemento in elementos[0]:  # ¿Ya existe el elemento en el universo?
                    if conjunto == "U":  # Si existe y se quiere agregar Universo
                        print("Este elemento ya existe en el conjunto Universo")

                    elif (
                        elemento in elementos[indice]
                    ):  # Si existe y tambien en el nuevo conjunto
                        print(f"{elemento} ya existe en {elementos[indice]}")
                    else:  # el elemento existe en el universo, no en el conjunto indicado
                        elementos[indice].append(elemento)
                        print("elemento añadido con exito")
                else:  # El elemento no existe en el universo
                    if conjunto == "U":  # se quiere añadir en el conjunto universo
                        elementos[0].append(elemento)
                        print("Elemento añadido con existo al conjunto Universo")

                    else:  # El elemento no existe en el universo y el conjunto no es el universo
                        print("Este elemento no existe en el conjunto universo")
            else:
                if len(elementos[indice]) == 0:
                    print("Ingrese al menos un elmeneto por conunto")
                else:
                    añadirMas = False
        else:
            añadirMas = False
            print(f"el conjunto {conjunto} ya tiene 10 elementos")
    limpiar_consola()


def crearUnion(nombre1, nombre2):

    conjunto1 = set(elementos[nombreconjuntos.index(nombre1)])
    conjunto2 = set(elementos[nombreconjuntos.index(nombre2)])
    
    union = list(conjunto1 | conjunto2)

    print(union)


def crearInterseccion(nombre1, nombre2):
    conjunto1 = set(elementos[nombreconjuntos.index(nombre1)])
    conjunto2 = set(elementos[nombreconjuntos.index(nombre2)])
    interseccion = list(conjunto1 & conjunto2)

    print(interseccion)


def crearDiferencia(nombre1, nombre2):
    conjunto1 = set(elementos[nombreconjuntos.index(nombre1)])
    conjunto2 = set(elementos[nombreconjuntos.index(nombre2)])
    diferencia = list(conjunto1 - conjunto2)

    print(diferencia)


def crearDiferenciaSimetrica(nombre1, nombre2):
    conjunto1 = set(elementos[nombreconjuntos.index(nombre1)])
    conjunto2 = set(elementos[nombreconjuntos.index(nombre2)])
    difSimetrica = list(conjunto1 ^ conjunto2)

    print (difSimetrica)


def crearComplemento(nombre):
    complemento = crearDiferencia("U", nombre)

    print(complemento)

def crearProductoEscalar(nombre1, nombre2):
    conjunto1 = list(elementos[nombreconjuntos.index(nombre1)])
    conjunto2 = list(elementos[nombreconjuntos.index(nombre2)])
    productoEscalar=[]
    for elemento1 in conjunto1:
        for elemento2 in  conjunto2:
            productoEscalar.append(f"({elemento1}, {elemento2})")
        
    
    print(productoEscalar)
    
    

# Funciones para apariencia Grafica
def cabecera():
    print(
        """
+===================================+
| ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗╔═╗ |
| ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║║║ ║╠╦╝╠═╣ |
| ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩═╩╝╚═╝╩╚═╩ ╩ |
|               ╔╦╗╔═╗              |
|                ║║║╣               |
|               ═╩╝╚═╝              |
|     ╔═╗╔═╗╔╗╔ ╦╦ ╦╔╗╔╔╦╗╔═╗╔═╗    |
|     ║  ║ ║║║║ ║║ ║║║║ ║ ║ ║╚═╗    |
|     ╚═╝╚═╝╝╚╝╚╝╚═╝╝╚╝ ╩ ╚═╝╚═╝    |
+===================================+
"""
    )


def main():

    cabecera()
    print("PARA INICIAR INGRESE LOS ELEMENTOS DEL CONJUNTO UNIVERSO")
    añadirElemento("U")

    maxConjuntos = int(input("INGRESE EL TOTAL DE CONJUNTOS A CREAR: "))
    contador = 1
    while contador <= maxConjuntos:
        nombreNuevo = input(f"Ingrese el nombre del conjunto #{contador}: ")
        if crearConjunto(nombreNuevo):
            añadirElemento(nombreNuevo)
            contador = contador + 1

    noSalir = True
    conjunto1 = ""
    conjunto2=""

    while noSalir:
        cabecera()
        print("CONJUNTOS DISPONIBLES:")
        for conjunto in nombreconjuntos:
            print(f"{conjunto}: {elementos[nombreconjuntos.index(conjunto)]}")
        print(
            """SELECCIONE UNA OPCION DEL MENÚ
              1. ELEGIR CONJUNTOS
              2. UNION
              3. INTERSECCION
              4. DIFERENCIA
              5. DIFERENCIA SIMETRICA
              6. COMPLEMENTO
              7. PRODUCTO ESCALAR
              8. SALIR"""
        )
        opcionElegida=int(input("INGRESE LA OPCION DESEADA: "))
        
        if opcionElegida == 1:
            conjunto2=""
            conjunto1 = ""
            
            while not(conjunto1 in nombreconjuntos and conjunto2 in nombreconjuntos):
                conjunto1= input("INGRESE EL NOMBRE DEL CONJUNTO #1: ")
                conjunto2 = input("INGRESE EL NOMBRE DEL CONJUNTO: #2: ")
                
                if not(conjunto1 in nombreconjuntos):
                    print("El conjunto #1 no es valido intente de nuevo")
                    conjunto1=""
                
                if not(conjunto2 in nombreconjuntos):
                    print("El conjunto #2 no es valido intente de nuevo")
                    conjunto2=""
                
        elif opcionElegida != 1 and opcionElegida!=8:
            if conjunto1 !="" and conjunto2!="":
                if opcionElegida == 2:
                    crearUnion(conjunto1,conjunto2)
                elif opcionElegida==3:
                    crearInterseccion(conjunto1,conjunto2)
                elif opcionElegida==4:
                    crearDiferencia(conjunto1,conjunto2)
                elif opcionElegida==5:
                    crearDiferenciaSimetrica(conjunto1,conjunto2)
                elif opcionElegida==6:
                    print(f"Conjunto Complemento de {conjunto1}")
                    crearComplemento(conjunto1)
                    print(f"Conjunto Complemento de {conjunto2}")
                    crearComplemento(conjunto2)
                elif opcionElegida==7:
                    crearProductoEscalar(conjunto1,conjunto2)
                else:
                    print("LA OPCION ELEGIDA NO ES VALIDA")
            else:
                print("LOS NOMBRES DE LOS CONJUNTOS NO SON VALIDOS")
        elif opcionElegida==8:
                noSalir=False
        aux = input("PRESIONE ENTER PARA CONTINUAR")
        limpiar_consola()


if __name__ == "__main__":
    main()