/*
CREACIÓN
MODIFICACION
    AÑADIR ELEMENTOS
    ELIMINAR ELEMENTOS
    ELIMINIAR CONJUNTOS
DIFERENCIA SIMETRICA
*/

let conjuntos = ["U"]; //Por defecto siempre existira el conjunto universo
let elementos = [[]]; //Indice 0 corresponde al conjunto universo inicialmente vacio

/** CREACION DE CONJUNTOS
 * CONSTARA DE 2 PARTES
 *  1 CREAR EL CONJUNTO
 *  2 AÑADIR LOS ELEMENTOS
 *
 */

//Creacion de Conjuntos
function crearConjuntos(nombre) {
  nombre = nombre.toUpperCase();
  if (conjuntos.includes(nombre)) {
    alert(`el conjunto ${nombre} ya existe`);
  } else {
    conjuntos.push(nombre);
    elementos.push([]); // Crea un array vacio en elementos donde se guardaran los elementos del conjunto recien guardado
  }
}

//Añadir Elementos
function añadirElementos(conjunto, elemento) {
    conjunto = conjunto.toUpperCase();
  // Primero verificar que el elemento exista en el conjunto Universo
  u = elementos[0];
  if (u.includes(elemento)) {
    //el elemento si existe en el conjunto universo
    if (conjunto === "U") {
      //se quiere agregar al conjunto universo
      alert(`El elemento ${elemento}, ya existe en el conjunto ${conjunto}`);
    } else {
      //se quier eagregar a otro conjunto
      indice = conjuntos.indexOf(conjunto);

      if (elementos[indice].length <= 9) {
        //verificar que el conjunto tiene menos de 10 elementos
        if (elementos[indice].includes(elemento)) {
          alert(
            `El elemento ${elemento}, ya existe en el conjunto ${conjunto}`
          );
        } else {
          elementos[indice].push(elemento);
          //elemento añadido
        }
      } else {
        alert(`El conjunto ${conjunto} ya tiene 10 elementos`);
      }
    }
  } else {
    //el elemento no existe en el universo
    if (conjunto === "U") {
      if (u.length <= 9) {
        elementos[0].push(elemento);
      } else {
        alert(`El conjunto ${conjunto} ya tiene 10 elementos`);
      }
    } else {
      alert(`El elemento ${elemento} no es parte del universo`);
    }
  }
}


//DIFERENCIA SIMETRICA
function diferenciaSimetrica(conjunto1, conjunto2){
  const dif12 = diferencia(conjunto1, conjunto2);
  const dif21 = diferencia(conjunto2, conjunto1);

  const conjuntoDiferenciaSimetrica = unirConjuntos(dif12,dif21);

  return conjuntoDiferenciaSimetrica;
}
