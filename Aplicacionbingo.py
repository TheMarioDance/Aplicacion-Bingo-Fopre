import numpy as np

# Función para verificar si se ha completado un patrón ganador en un cartón.
def check_win(cardboard, pattern, marked):
    for r in range(5):
        for c in range(5):
            if pattern[r][c] and not marked[r][c]:
                return False  # Si hay una casilla del patrón que no está marcada, no se ha ganado
    return True  # Si todas las casillas del patrón están marcadas, se ha ganado


# Función para marcar las casillas correspondientes en todos los cartones.
def mark_cardboards(cardboards, called_letter, called_number, marked_list):
    for i, cardboard in enumerate(cardboards):  # Iterar sobre cada cartón
        marked = False  # Bandera para controlar si el número ya ha sido marcado en este cartón
        for r in range(5):  # Iterar sobre las filas
            for c in range(5):  # Iterar sobre las columnas
                if cardboard[r][c] == (called_letter, called_number):  # Verificar coincidencia
                    marked_list[i][r][c] = True  # Marcar la casilla
                    marked = True  # Actualizar la bandera
                    break  # Pasar al siguiente cartón (opcional, para mayor eficiencia)
            if marked:
                break  # Salir del bucle exterior si ya se marcó el número en este cartón


# Función para imprimir todos los cartones.
def print_boards(cardboards, marked_list):
    for i, cardboard in enumerate(cardboards):
        print(f"\nCartón {i + 1}:")  # Imprimir el número de cartón
        for r in range(5):
            row_str = ""
            for c in range(5):
                if marked_list[i][r][c]:
                    row_str += "X "  # Marcar con 'X' si está marcado
                elif r == 2 and c == 2:
                    row_str += "J "  # Marcar con 'J' si es el comodín (igual el comodín se encuentra marcado por defecto)
                else:
                    row_str += str(cardboard[r][c][1]) + " " if cardboard[r][c][1] is not None else "__ "  # Mostrar "__" si está libre
            print(row_str)


# Configuraciones de los cartones (agregue otros cartones de manera similar)
cardboard1 = [
    [('F', 10), ('O', 27), ('P', 35), ('R', 50), ('E', 74)],
    [('F', 15), ('O', 28), ('P', 37), ('R', 47), ('E', 68)],
    [('F', 2), ('O', 29), (None, None), ('R', 59), ('E', 72)],
    [('F', 11), ('O', 24), ('P', 31), ('R', 54), ('E', 75)],
    [('F', 5), ('O', 17), ('P', 42), ('R', 55), ('E', 63)]
]

cardboard2 = [
    [('F', 1), ('O', 25), ('P', 33), ('R', 49), ('E', 64)],
    [('F', 7), ('O', 23), ('P', 35), ('R', 58), ('E', 63)],
    [('F', 6), ('O', 20), (None, None), ('R', 51), ('E', 61)],
    [('F', 11), ('O', 28), ('P', 42), ('R', 54), ('E', 69)],
    [('F', 15), ('O', 18), ('P', 43), ('R', 53), ('E', 72)]
]

cardboard3 = [
    [('F', 7), ('O', 27), ('P', 32), ('R', 53), ('E', 70)],
    [('F', 14), ('O', 28), ('P', 36), ('R', 59), ('E', 75)],
    [('F', 4), ('O', 18), (None, None), ('R', 57), ('E', 61)],
    [('F', 2), ('O', 22), ('P', 43), ('R', 46), ('E', 71)],
    [('F', 5), ('O', 16), ('P', 44), ('R', 51), ('E', 74)]
]

cardboard4 = [
    [('F', 7), ('O', 29), ('P', 43), ('R', 57), ('E', 61)],
    [('F', 13), ('O', 17), ('P', 36), ('R', 56), ('E', 65)],
    [('F', 4), ('O', 21), (None, None), ('R', 58), ('E', 64)],
    [('F', 9), ('O', 30), ('P', 34), ('R', 48), ('E', 67)],
    [('F', 15), ('O', 22), ('P', 37), ('R', 55), ('E', 68)]
]

cardboards = [cardboard1, cardboard2, cardboard3, cardboard4]  # Lista de todos los cartones

# Patrones ganadores
patterns = {
    'F': [
        [True, False, False, False, False],
        [True, False, False, False, False],
        [True, False, True, False, False],
        [True, False, False, False, False],
        [True, False, False, False, False],
    ],
    'completo': [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    'O': [
        [True, True, True, True, True],
        [True, False, False, False, True],
        [True, False, True, False, True],
        [True, False, False, False, True],
        [True, True, True, True, True],
    ],
    'P': [
        [True, True, True, True, True],
        [True, False, False, False, True],
        [True, True, True, True, True],
        [True, False, False, False, False],
        [True, False, False, False, False],
    ],
    'R': [
        [True, True, True, True, True],
        [True, False, False, False, False],
        [True, False, True, False, False],
        [True, False, False, False, False],
        [True, False, False, False, False],
    ]
}

# Inicialización del juego
current_pattern = patterns.get(input("Ingrese el patrón a buscar (F, O, P, R, completo): "))
if current_pattern is None:
    print("Patrón no válido. Saliendo.")
    exit()

marked_list = [np.full((5, 5), False) for _ in range(len(cardboards))]  # Una matriz marcada para cada cartón
for i in range(len(cardboards)):
    marked_list[i][2, 2] = True  # Marcar el comodín en cada cartón


while True:
    called_input = input("Ingrese el número llamado (ej. F15, pulse Enter para saltar o escriba 'salir' para terminar): ").upper()
    if not called_input:  # Manejar input vacío (cuando se da enter)
        continue

    if called_input == "SALIR":  # Condición de salidaa
        print("Saliendo del juego.")
        break # Salida del loop

    try:
        letter = called_input[0]
        number = int(called_input[1:])
        mark_cardboards(cardboards, letter, number, marked_list)
        print_boards(cardboards, marked_list)

        for i in range(len(cardboards)):
            if check_win(cardboards[i], current_pattern, marked_list[i]):
                print(f"¡Cartón {i + 1} gana!")
                another_game = input("¿Jugar otra partida (si/no)? ").lower()
                if another_game != 'si':
                    exit()  # Solo se sale si se quiere jugar otra partida
                else:  # Reinicio para un nuevo juego
                    current_pattern = patterns.get(input("Ingrese el patrón a buscar (F, O, P, R, completo): "))
                    if current_pattern is None:
                        print("Patrón no válido. Saliendo.")
                        exit()
                    marked_list = [np.full((5, 5), False) for _ in range(len(cardboards))]  # Una matriz marcada para cada cartón
                    for j in range(len(cardboards)):
                        marked_list[j][2, 2] = True  # Marcar el comodín en cada cartón
                    break  # Salir del inner loop para empezar un nuevo juego



    except (ValueError, IndexError):
        print("Entrada inválida. Por favor, ingrese un número válido (ej. F15).")