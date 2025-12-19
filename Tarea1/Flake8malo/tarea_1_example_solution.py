"""
Archivo: tarea_1_solution.py

Este archivo contiene modulos para:
1) Ejecutar operaciones básicas entre dos números enteros.
2) Calcular el promedio de una lista de valores numéricos.

Cada función retorna un código de estado y resultado según la función.
"""


def operation_selector(num1, num2, op):
    """
    Ejecuta una operación entre dos números enteros según el operador indicado.

    Parámetros de entrada:
        num1 (int): primer operando
        num2 (int): segundo operando
        op (str): operador de la operación
                  "+" suma
                  "-" resta
                  "*" multiplicación
                  "&" AND

    Retorna como salidas:
        (codigo, resultado)
        codigo:
            0   -> operación exitosa
           -50  -> num1 o num2 no es un entero válido
           -60  -> operador ingresado no es string
           -70  -> operador no soportado
        resultado:
            resultado de la operación o None si ocurre un error
    """
    # Valor por defecto del resultado
    resultado = None

    # Validación de los operandos
    # Se verifica que ambos sean enteros y que no sean booleanos
    if not isinstance(num1, int) or isinstance(num1, bool):
        return -50, resultado
    if not isinstance(num2, int) or isinstance(num2, bool):
        return -50, resultado
    # Validación del operador
    if not isinstance(op, str):
        return -60, resultado

    # Selección de la operación
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "&":
        resultado = num1 & num2
    else:
        # Operador no reconocido
        return -70, resultado

    return 0, resultado


def calculo_promedio(lista_valores):
    """
    Calcula el promedio de una lista de valores numéricos.

    Parámetro de entrada:
        lista_valores (list): lista con números enteros o floats

    Retorna como salidas:
        (codigo, resultado)
        codigo:
            0   -> promedio calculado correctamente
           -80  -> algún elemento no es numérico válido
           -90  -> la lista tiene más de 10 elementos
        resultado:
            promedio de la lista o None si ocurre un error
    """

    # Valor por defecto del resultado
    resultado = None

    # Validación del tamaño de la lista
    if len(lista_valores) > 10:
        return -90, resultado

    # Validación de los elementos de la lista
    for valor in lista_valores:
        # Se aceptan datos de tipo int y float, pero no valores booleanos
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return -80, resultado

    # Se evita la división por cero si la lista está vacía
    if len(lista_valores) == 0:
        return -80, resultado

    # Cálculo del promedio
    resultado = sum(lista_valores) / len(lista_valores)

    return 0, resultado
