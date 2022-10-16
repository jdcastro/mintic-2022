#!/usr/bin/env python

def sumapositivos(a: int, b: int) -> int:
    """ Procesa dos números enteros y devuelve la suma de los dos.
    Args:
        a: int
        b: int
    Returns:
    a: resultado de la suma de los dos números a + b
    >>> sumapositivos(1, 2)
    3
    >>> sumapositivos(100, 2)
    102

    """
    assert a >= 0 and b >= 0, "Los números deben ser positivos" 
    return a + b
try:
    print (sumapositivos(int(input("Ingresa número")), int(input("Ingresa un número: "))))
except AssertionError as msg:
    print(msg)


