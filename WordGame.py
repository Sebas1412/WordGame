# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:32:49 2020

@author: Federico
"""

import math
import random


VOCALES = 'aeiou'
CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
TAMANIO_MANO = 7

VALORES_LETRAS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'ñ': 4, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Codigo de ayuda
#

ARCHIVO_PALABRAS = 'WordGame\WordGame\palabras.txt'

def cargar_palabras():
    """
    Retorna una lista de palabras válidas, compuestas por letras en minúscula.
    
    Dependiendo del tamaño de la lista de palabras, esta función puede tomarse su tiempo para finalizar.
    """
    
    print("Cargando lista de palabras desde el archivo...")
    # inFile: Archivo
    inFile = open(ARCHIVO_PALABRAS, 'r', encoding='UTF-8')
    # palabras: lista de cadenas
    palabras = []
    for palabra in inFile:
        palabras.append(palabra.strip().lower())
    print("  ", len(palabras), "palabras cargadas.")
    return palabras

def obtener_diccionario_frecuencias(secuencia):
    """
    Genera un diccionario donde las claves son los elementos de la secuencia
    y los valores son enteros, que indican la cantidad de veces que ese
    elemento está repetido en la secuencia.

    secuencia: cadena o lista
    return: diccionario {tipo_elemento -> int}
    """
    
    # frecuencias: diccionario
    frec = {}
    for x in secuencia:
        frec[x] = frec.get(x,0) + 1
    return frec
	
#
# (fin Codigo de ayuda)
# -----------------------------------

#
# Problema #2: Puntuar una palabra
#
def obtener_puntaje_palabra(palabra, n):
    """
    Obtiene el puntaje de una palabra. Asume que la palabra es una palabra válida.

    Podemos asumir que la palabra siempre será una cadena de letras 
    o la cadena vacía (""). No se puede asumir que solo contendrá letras en
    minúsculas, así que deberemos resolver también con palabras con letras en
    mayúscula y minúscula.
    
	El puntaje de una palabra es el producto de dos componentes:

	Primer componente: la suma de los puntos de las letras en la palabra.
    Segundo componente: 1 o la fórmula 
        [7 * longitud_palabra - 3 * (n - longitud_palabra)], el valor que 
    sea más grande, donde longitud_palabra es la cantidad de letras usadas 
    en la palabra y n es la cantidad de letras disponibles en la mano actual.

    Al igual que en Scrabble, cada letra tiene un puntaje.

    palabra: cadena
    n: int >= 0
    retorna: int >= 0
    """
    palabra = palabra.lower()
    suma_letras = 0
    VALORES_LETRAS['*'] = 0
    for letra in palabra:
        suma_letras += VALORES_LETRAS[letra]
    
    segundo_componente = max((7 * len(palabra) - 3 * (n - len(palabra))), 1)
    
    puntaje_palabra = suma_letras * segundo_componente
    
    return puntaje_palabra
    

def mostrar_mano(mano):
    """
    Muestra las letras que están en la mano del jugador.

    Por ejemplo:
       mostrar_mano({'a':1, 'x':2, 'l':3, 'e':1})
    Debería mostrar por consola lo siguiente:
       a x x l l l e
    El orden de las letras no es importante.

    mano: diccionario (string -> int)
    """
    
    for letra in mano.keys():
        for j in range(mano[letra]):
            print(letra, end=' ')      # Muestra todas las letras en la misma linea
    print()                             # Linea vacía


def repartir_mano(n):
    """
    Genera una mano al azar con n letras en minúscula.
    techo(n/3) letras en la mano deben ser VOCALES.

    Las manos se representan como diccionarios. Las claves son letras 
    y los valores indican el número de veces que esa letra está contenida 
    en la mano.

    n: int >= 0
    Retorna: diccionario (string -> int)
    """
    
    mano={}
    cantidad_vocales = int(math.ceil(n / 3))

    for i in range(cantidad_vocales-1):
        x = random.choice(VOCALES)
        mano[x] = mano.get(x, 0) + 1
    
    mano['*'] = 1
    
    for i in range(cantidad_vocales, n):    
        x = random.choice(CONSONANTES)
        mano[x] = mano.get(x, 0) + 1
    
    return mano

#
# Problema #3: Actualizar la mano eliminando letras.
#
def actualizar_mano(mano, palabra):
    """
    NO asumir que la mano contiene el mismo número de veces una letra 
    que las que aparece en la palabra. Las letras que están en la palabra 
    y no en la mano deben ser ignoradas. Las letras que aparecen más veces 
    en la palabra que en la mano no deben resultar en un total negativo; 
    debemos eliminar esa letra de la mano o poner su cantidad en 0.

    Actualiza la mano: usa las letras que están en la palabra y retorna 
    la nueva mano, sin esas letras.

    No debe modificar mano, sino que debe retornar un nuevo diccionario.

    palabra: string
    mano: diccionario (string -> int)    
    retorna: diccionario (string -> int)
    """
    palabra_minuscula = palabra.lower()
    mano_copia = mano.copy()
    nueva_mano = {}
    for clave in mano_copia.keys():
        if clave not in set(palabra_minuscula):
            nueva_mano[clave] = mano_copia[clave]
        elif  clave in list(palabra_minuscula):
            if mano_copia[clave] > 1:
                nueva_mano[clave] = mano_copia[clave] - list(palabra_minuscula).count(clave)
                if nueva_mano[clave] == 0:
                    nueva_mano.pop(clave)
    
            
        
    return nueva_mano



    

#
# Problema #4: Verificar si la palabra es válida.
#
def es_palabra_valida(palabra, mano, lista_palabras):

    """
    Devuelve True si la palabra está en lista_palabras y está compuesta
    completamente por letras en la mano. Sino, devuelve False.
    No se debe modificar ni mano ni lista_palabras.
   
    palabra: string
    mano: diccionario (string -> int)
    lista_palabras: lista de cadenas en minúsculas
    Retorna: booleano
    """
    VALORES_LETRAS['*'] = 0
    palabra_minuscula = palabra.lower()
    booleano = True
    if palabra_minuscula not in lista_palabras:
        booleano = False
        for vocal in VOCALES:
            if palabra_minuscula.replace('*', vocal) in lista_palabras:
                booleano = True  
    for letra in palabra_minuscula:
        if letra not in mano.keys() or palabra_minuscula.count(letra) > mano[letra]:
            booleano = False 
    
    return booleano

#
# Problema #5: Jugar una mano
#
def calcular_longitud_mano(mano):
    """ 
    Retorna la longitud (cantida de letras) en la mano actual.
    
    mano: diccionario (string-> int)
    retorna: integer
    """
    return sum(mano.values())

def jugar_mano(mano, lista_palabras):

    """
    Permite que un usuario juegue una mano, con las siguientes consideraciones:


    * Se le muestra la mano actual.
    
    * El usuario puede ingresar una palabra.

    * Cuando una palabra es ingresada (válida o inválida), utiliza letras de la mano.

    * Una palabra inválida se rechaza, mediante un mensaje que le pide al usuario
      que ingrese otra palabra.

    * Después de cada palabra válida: se muestra el puntaje de la palabra, 
      las letras restantes de la mano y se le pide al usuario que ingrese 
      otra palabra.

    * La suma de los puntajes de las palabras se presenta una vez que la mano termina.

    * La mano termina cuando no hay más letras sin usar.
      El usuario también puede terminar la mano ingresando dos signos de exclamación
      ('!!') en vez de una palabra.

      mano: diccionario (string -> int)
      lista_palabras: lista de cadenas en minúsculas.
      retorna: el puntaje total de la mano

      
    """
    
    
    #print('Mano actual: ') 
    
    #mostrar_mano(mano)

    palabra = input('Ingrese una palabra o !! si desea terminar: ')
    puntaje_total = 0
    puntaje_parcial = 0
    n = calcular_longitud_mano(mano)
    while palabra != '!!' and calcular_longitud_mano(mano) != 0:
        
        if es_palabra_valida(palabra, mano, lista_palabras) == True:
            puntaje_parcial = obtener_puntaje_palabra(palabra, n)
            puntaje_total += puntaje_parcial
            print(f'{palabra} resulta en {puntaje_parcial} puntos. Total: {puntaje_total} puntos')
            mano = actualizar_mano(mano, palabra)
            n  = calcular_longitud_mano(mano)
            if calcular_longitud_mano(mano) == 0:
                print('Se quedó sin letras')
            else: 
                print('Mano actual:' ), mostrar_mano(mano)
                palabra = input('ingrese una palabra o !! si desea terminar: ')
        else:
            print(f'{palabra} no es una palabra válida, por favor ingrese otra palabra')
            mano = actualizar_mano(mano, palabra)
            n  = calcular_longitud_mano(mano)
            if calcular_longitud_mano(mano) == 0:
                print('Se quedó sin letras')
            else: 
                print('Mano actual:' ), mostrar_mano(mano)
                palabra = input('ingrese una palabra o !! si desea terminar: ')
    
        
    return puntaje_total




       
    
    # PSEUDO-CODIGO
    # Llevar registro del puntaje total
    
    # Mientras haya letras en la mano o el usuario no ingrese '!!':
    
        # Mostrar la mano
        
        # Pedirle al usuario que ingrese una palabra
        
        # Si la entrada son dos signos de exclamación, se termina el juego
                    
        # Sino (la entrada no son dos signos de exclamación):

            # Si la palabra es válida:

                # Mostrarle al usuario los puntos que ganó,
                # y el puntaje total de la mano hasta ese momento.

            # Sino (la palabra no es válida):
                # Rechazar palabra inválida (mostrar un mensaje)
                
            # actualizar la mano del usuario eliminando las letras 
            # que usó en la palabra (aún si la palabra era inválida)
            

    # Se terminó el juego (el usuario se quedó sin letras o ingresó '!!'),
    # se le muestra el puntaje final de la mano.

    # Retorna el puntaje final como resultado de la función.



#
# Problema #6: Jugar una partida completa
# 


#
# procedimiento para reemplazar una letra en la mano
#

def intercambiar_mano(mano, letra):
    """
    Permite al usuario reemplazar todas las copias de una letra en la mano 
    (elegida por el usuario) por una nueva letra elegida, al azar, de VOCALES 
    y CONSONANTES. La nueva letra debe ser diferente a la elegida para intercambiar, 
    y no puede ser ninguna de las letras que ya tiene en la mano.
    
    Si el usuario ingresa una letra que no está en la mano, la mano debe quedar igual.
    
    No se debe modificar la mano original.
    Por ejemplo:
        intercambiar_mano({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    puede resultar en:
        {'h':1, 'e':1, 'o':1, 'x':2} -> si la nueva letra es 'x'
    La nueva letra no debe ser 'h', 'e', 'l', u 'o' ya que esas letras ya están en 
    la mano.
    
    mano: diccionario (string -> int)
    letra: string
    retorna: diccionario (string -> int)
    """

    while letra not in mano.keys():
        print(f'{letra}, no se encuentra en la mano, elija una opción válida')
        letra = input('Qué letra desa intercambiar: ')
    nueva_letra = random.choice(list(set(VALORES_LETRAS.keys()).difference(mano.keys())))
    mano[nueva_letra] = mano[letra]
    del(mano[letra])
    return mano
    
   

#
# Problema #1: Armar esqueleto del ciclo de juego
#       
    
def jugar_partida(lista_palabras):
    """
    Permitir al usuario jugar una serie de manos (partida)

    * Pedir al usuario que ingrese un número total de manos.
    

    * Acumular el puntaje de cada mano en un puntaje total para la partida.
 
    * Por cada mano, antes de empezar a jugar, preguntar al usuario si quiere
      intercambiar una letra por otra. Esto se puede hacer sólo una vez durante 
      el juego. Una vez que se usa esta opción, no se le debe preguntar nuevamente 
      al usuario si quiere intercambiar una letra durante el juego.
    
    * Por cada mano, preguntar al usuario si desea volver a jugar la mano.
      Si el usuario ingresa 'si', se repetirá la mano y se mantendrá el mayor
      de los dos puntajes obtenidos para esa mano. Esto se puede hacer una única vez
      durante la partida. Una vez que se utiliza la opción de volver a jugar una mano,
      no se debe volver a preguntar si desea volver a jugar futuras manos. Volver a
      jugar una mano no afecta el número de manos totales que el usuario eligió jugar.
      
            * Nota: si se vuelve a jugar una mano, no se podrá elegir reemplazar una
              letra (se debe jugar con la mano original)
      
    * Devuelve el puntaje total de la partida.

    lista_palabras: lista de cadenas en minúsculas
    """
    puntaje_mano = 0
    puntaje_final = 0
    nro_mano = 0
    contador = 0
    manos_a_jugar = input('Ingrese la cantidad de manos que desea jugar: ')
    #try:
    if int(manos_a_jugar) > 0:
        
        manos_a_jugar = int(manos_a_jugar)
        while manos_a_jugar > contador:
            mano_repetida = False
            intercambio = False
            nro_mano +=1
            print(f"Jugando mano nro: {nro_mano}")
            mano = repartir_mano(TAMANIO_MANO)
            print('Mano actual:')
            mostrar_mano(mano)
            mano_original = mano.copy()   
            if intercambio == False:
                intercambiar = input('Desea intercambiar letra?: (si/no)')
                if intercambiar == 'si':
                    letra = input('ingresar letra a cambiar: ')
                    print('Intercambiando letra')
                    mano_cambiada = intercambiar_mano(mano, letra)
                    print('Mano actual: ')
                    mostrar_mano(mano_cambiada)
                    puntaje_mano += jugar_mano(mano_cambiada,lista_palabras)
                    puntaje_final += puntaje_mano
                    intercambio == True  
                else:
                    print('Mano actual: ')
                    mostrar_mano(mano)
                    puntaje_mano += jugar_mano(mano, lista_palabras)
                    puntaje_final += puntaje_mano 

            if mano_repetida == False:
                repetir = input('Desea repetir la mano actual?: (si/no)')
                if repetir == 'si':
                    puntaje_final -= puntaje_mano
                    puntaje_mano = 0
                    print('Mano actual: ')
                    mostrar_mano(mano_original)
                    intercambiar = input('Desea intercambiar letra?: (si/no)')
                    if intercambiar == 'si':
                        letra = input('ingresar letra a cambiar: ')
                        print('Intercambiando letra')
                        mano_cambiada = intercambiar_mano(mano_original, letra)
                        print('Mano actual: ')
                        mostrar_mano(mano_cambiada)
                        puntaje_mano += jugar_mano(mano_cambiada,lista_palabras)
                        puntaje_final += puntaje_mano    
                    else:
                        puntaje_mano = 0
                        puntaje_mano = jugar_mano(mano_original, lista_palabras)
                        puntaje_final += puntaje_mano
                        mano_repetida = True     
                else:
                    print(f'Puntaje final de la mano: {puntaje_mano} puntos')
            contador += 1
            puntaje_mano = 0
                
        #puntaje_final += puntaje_mano
        
    else:
        print(f'{int(manos_a_jugar)} no es valido, ingrese un nro mayor a 0')
        #except:
        #    print (f'{(manos_a_jugar)} no es valido, ingrese un nro mayor a 0')
    return print(f'El puntaje final de la partida es de: {puntaje_final}')   
        


    


#
# Construye las estructuras de datos necesarias para jugar la partida.
# No eliminar la condición "if __name__ == '__main__':" Este código se ejecuta
# cuando el programa se ejecuta directamente, sin usar la sentencia import.
#

if __name__ == '__main__':
    lista_palabras = cargar_palabras()
    jugar_partida(lista_palabras)