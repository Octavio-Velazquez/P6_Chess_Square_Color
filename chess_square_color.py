
def getChessSquareColor(column, row):
    """Returns black or white depending on the column and row."""

    # Revisa si las columnas y filas tienen números mayores a los permitidos.
    if (column < 0) or (column > 7):
        return "There is an error."
    if (row < 0) or (row > 7):
        return "There is an error"

    # Compara si la columna es igual a 0 y revisa el valor de las filas.
    if (column == 0) and (row % 2 == 1):
        return "Negro"
    elif (column == 0) and (row % 2 == 0):
        return "Blanco"

    # Revisa si la columna tiene un número impar y el valor que tenga la fila.
    if (column % 2 == 1) and (row == 0):
        return "Negro"
    elif (column % 2 == 1) and (row % 2 == 1):
        return "Blanco"
    elif (column % 2 == 1) and (row % 2 == 0):
        return "Negro"

    # Revisa si la columna tiene un número par y el valor que tenga la fila.
    if (column % 2 == 0) and (row == 0):
        return "Blanco"
    elif (column % 2 == 0) and (row % 2 == 1):
        return "Negro"
    elif (column % 2 == 0) and (row % 2 == 0):
        return "Blanco"

print(getChessSquareColor(5,7))