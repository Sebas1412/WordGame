# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:42:33 2020

@author: Federico
"""

import WordGame
#
# Código para testeos
#

def test_obtener_puntaje_palabra():
    """
    Test de unidad para obtener_puntaje_palabra
    """

    # diccioario de palabras y puntajes
    mensaje = "\tSe esperaban {0} puntos pero se obtuvieron '{1}' para la palabra:  '{2}', con n={3}"
    
    palabras = {("", 7):0, ("mi", 7):4, ("que", 7):108, ("quien", 6):448,
             ("puntos", 7):312, ("CabeZA", 7):741, ("Cuenta", 7):312,
             ("tenedor", 7):392, ("CUAL", 4):168, ("mico", 6):176}
    for (palabra, n) in palabras.keys():
        puntaje = WordGame.obtener_puntaje_palabra(palabra, n)
        assert puntaje == palabras[(palabra, n)], mensaje.format(palabras[(palabra, n)],str(puntaje), palabra, n)

# fin de test_obtener_puntaje_palabra


def test_actualizar_mano():
    """
    Test de unidad para actualizar_mano
    """
    # test 1
    mano_orig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'o':1}
    mano_copia = mano_orig.copy()
    palabra = "malo"

    mano_nueva = WordGame.actualizar_mano(mano_copia, palabra)
    mano_esperada1 = {'q':1, 'l':1, 'u':1}
    mano_esperada2 = {'a':0, 'q':1, 'l':1, 'm':0, 'u':1, 'o':0}
    
    mensaje = "\tSe obtuvo: {0}\n\t-- pero se esperaba:{1} o {2}"
    print("test_actualizar_mano('"+ palabra +"', " + str(mano_orig) + ")")
    assert mano_nueva == mano_esperada1 or mano_nueva == mano_esperada2, mensaje.format(mano_nueva, mano_esperada1, mano_esperada2)

    assert mano_copia == mano_orig, "\tImplementación de actualizar_mano modificó la mano original!"
        
    # test 2
    mano_orig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    mano_copia = mano_orig.copy()
    palabra = "Veni"

    mano_nueva = WordGame.actualizar_mano(mano_copia, palabra)
    mano_esperada1 = {'v':1, 'l':2}
    mano_esperada2 = {'e':0, 'v':1, 'n':0, 'i':0, 'l':2}
    
    print("test_actualizar_mano('"+ palabra +"', " + str(mano_orig) + ")")
    assert mano_nueva == mano_esperada1 or mano_nueva == mano_esperada2, mensaje.format(mano_nueva, mano_esperada1, mano_esperada2)

    assert mano_copia == mano_orig, "\tImplementación de actualizar_mano modificó la mano original!"

    # test 3
    mano_orig = {'c': 1, 'e': 1, 'l': 2, 'a': 1}
    mano_copia = mano_orig.copy()
    palabra = "CALLE"

    mano_nueva = WordGame.actualizar_mano(mano_copia, palabra)
    mano_esperada1 = {}
    mano_esperada2 = {'c': 0, 'e': 0, 'l': 0, 'a': 0}
    
    print("test_actualizar_mano('"+ palabra +"', " + str(mano_orig) + ")")
    assert mano_nueva == mano_esperada1 or mano_nueva == mano_esperada2, mensaje.format(mano_nueva, mano_esperada1, mano_esperada2)

    assert mano_copia == mano_orig, "\tImplementación de actualizar_mano modificó la mano original!"
    
    # test 4
    mano_orig = {'c': 1, 'a': 1, 'l': 2, 'e': 1}
    mano_copia = mano_orig.copy()
    palabra = "calar"

    mano_nueva = WordGame.actualizar_mano(mano_copia, palabra)
    mano_esperada1 = {'l':1, 'e': 1}
    mano_esperada2 = {'c': 0, 'a': 0, 'l': 1, 'e': 1}
    
    print("test_actualizar_mano('"+ palabra +"', " + str(mano_orig) + ")")
    assert mano_nueva == mano_esperada1 or mano_nueva == mano_esperada2, mensaje.format(mano_nueva, mano_esperada1, mano_esperada2)

    assert mano_copia == mano_orig, "\tImplementación de actualizar_mano modificó la mano original!"

    print("EXITO: test_actualizar_mano()")

# fin de test_actualizar_mano

def test_es_palabra_valida():
    """
    Test de unidad para es_palabra_valida
    """
    lista_palabras = WordGame.cargar_palabras()
    
    # test 1
    palabra = "hola"
    mano_orig = WordGame.obtener_diccionario_frecuencias(palabra)
    mano_copia = mano_orig.copy()

    mensaje = "\tSe esperaba {0}, pero se obtuvo {1} para la palabra: '{2}' y mano:{3}"
    assert WordGame.es_palabra_valida(palabra, mano_copia, lista_palabras), mensaje.format(True, False, palabra, mano_orig)

    # Se hace un segundo test para verificar si lista_palabras o mano fueron modificados
    assert WordGame.es_palabra_valida(palabra, mano_copia, lista_palabras), "\timplementacion de es_palabra_valida modificó la mano original o la lista de palabras"

    # test 2
    mano = {'r': 3, 'e': 3, 'p': 2, 'e': 3, 't': 1, 'u':1}
    palabra = "Repercute"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    # test 3
    mano = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':2, 'w':1, 'e': 2}
    palabra = "donde"

    assert WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(True, False, palabra, mano)

    # test 4
    mano = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    palabra = "donde"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    # test 5
    mano = {'o':1, 'v':2, 'n':1, 'i':1, 'l':2}
    palabra = "VILO"
    
    assert  WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(True, False, palabra, mano)
        
    # test 6
    palabra = "Ovillo"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)
    
    # test 6
    mano = {'c':0, 'a':2, 's':2, 'l':1, 'd':0}
    palabra = "casa"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    print("EXITO: test_es_palabra_valida()")

# end of test_es_palabra_valida

def test_comodines():
    """
    Test de unidad para es_palabra_valida.
    """
    lista_palabras = WordGame.cargar_palabras()

    # test 1
    mano = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    palabra = "e*m"

    mensaje = "\tSe esperaba {0}, pero se obtuvo {1} para palabra: '{2}' y mano:{3}"
    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    # test 2
    mano = {'n': 1, 'h': 1, '*': 1, 'l': 1, 'd':1, 'w':1, 'a': 2}
    palabra = "hola"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    # test 3
    mano = {'n': 1, 'h': 1, '*': 1, 'l': 1, 'd':1, 'w':1, 'a': 2}
    palabra = "h*la"

    assert WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(True, False, palabra, mano)

    # test 4
    mano = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
    palabra = "c*wz"

    assert not WordGame.es_palabra_valida(palabra, mano, lista_palabras), mensaje.format(False, True, palabra, mano)

    # diccionario con palabras y puntajes con comodines.
    mensaje = "\Se esperaban {0} puntos pero se obtuvo '{1}' para palabra '{2}', con n={3}"
    palabras = {("cab*za", 7):702, ("Cuent*", 7):273, ("C*enta", 7):273, ("C*sa", 7):95}
    for (palabra, n) in palabras.keys():
        puntaje = WordGame.obtener_puntaje_palabra(palabra, n)
        assert puntaje == palabras[(palabra, n)], mensaje.format(palabras[(palabra, n)], puntaje, palabra, n)

    print("EXITO: test_comodines()")

def test_calcular_longitud_mano():
    """
    Test de unidad para calcular_longitud_mano.
    """
    
    mensaje = "\Se esperaban {0} letras en la mano pero se obtuvo '{1}'"
    
    # test 1
    mano = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
    longitud = 7
    resultado = WordGame.calcular_longitud_mano(mano)
    assert longitud == resultado, mensaje.format(longitud, resultado)

    # test 2
    mano = {'a': 0, 'r': 0, 'e': 2, 'j': 2, 'm': 1, '*': 0}
    longitud = 5
    resultado = WordGame.calcular_longitud_mano(mano)
    assert longitud == resultado, mensaje.format(longitud, resultado)
    
    # test 3
    mano = {'e': 2, 'j': 2, 'm': 1}
    longitud = 5
    resultado = WordGame.calcular_longitud_mano(mano)
    assert longitud == resultado, mensaje.format(longitud, resultado)

##Descomentar para correr los tests sin el plugin de unittest
#print("----------------------------------------------------------------------")
#print("Test para obtener_puntaje_palabra...")
#test_obtener_puntaje_palabra()
#print("----------------------------------------------------------------------")
#print("Test para actualizar_mano...")
#test_actualizar_mano()
#print("----------------------------------------------------------------------")
#print("Test para es_palabra_valida...")
#test_es_palabra_valida()
#print("----------------------------------------------------------------------")
#print("Test para comodines...")
#test_comodines()
#print("Test para calcular_longitud_mano...")
#test_calcular_longitud_mano()
#print("Terminado!")