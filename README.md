# Bingo Tracker para el Bingo FOPRE

Este programa en Python ayuda a seguir el progreso de un juego de Bingo FOPRE con múltiples cartones y diferentes patrones de victoria.

## Cómo usar

1.  **Instalación:**  Asegúrese de tener Python 3 instalado en su sistema.  Además, necesita la librería NumPy. Puede instalarla usando pip:

    ```bash
    pip install numpy
    ```

2.  **Ejecución:**  Guarde el código como un archivo Python (por ejemplo, `bingo.py`) y ejecútelo desde su terminal:

    ```bash
    python bingo.py
    ```

3.  **Configuración inicial:** El programa le pedirá que ingrese el patrón de victoria que se utilizará en la partida.  Las opciones son F, O, P, R o completo.

4.  **Juego:** Una vez iniciado, el programa le pedirá que ingrese los números que van saliendo.  Ingrese la letra y el número (ej. F15, O27) o pulse Enter para saltarse un turno. Si alguien ya ganó y desea terminar la partida antes, escriba "salir".

5.  **Resultados:** Después de cada número ingresado, el programa mostrará el estado de todos los cartones, marcando los números coincidentes con una "X" y el comodín con una "J". Si un cartón completa el patrón de victoria, el programa anunciará el ganador y preguntará si desea jugar otra partida.


## Cartones y Patrones

El código incluye cuatro cartones de ejemplo (`carton1`, `carton2`, `carton3`, `carton4`), que fue los que jugué en 2024.  Puede modificar estos cartones con sus propios números.  El centro de cada cartón se considera un comodín ("J") y siempre está marcado.

Los patrones de victoria están definidos en el diccionario `patterns`. Puede modificar o agregar nuevos patrones según sus necesidades.  Cada patrón se representa como una matriz de booleanos de 5x5, donde `True` indica que la casilla debe estar marcada para ganar.

## Consideraciones

*   Asegúrese de que los números en los cartones estén dentro del rango esperado y que las letras de las columnas sean correctas.
*   El programa no genera números aleatorios para el Bingo; debe ingresarlos manualmente.
*   Si necesita modificar la lógica del juego (ej. número de cartones, rango de números), puede ajustar el código fuente.

## Ejemplo de uso
Ingrese el patrón a buscar (F, O, P, R, completo): completo

Ingrese el número llamado (ej. F15, o pulse Enter para saltar o escriba salir para terminar antes): F10
... (se muestran los cartones con las marcas)

Ingrese el número llamado (ej. F15, o pulse Enter para saltar o escriba salir para terminar antes): O27
... (se muestran los cartones con las marcas)

... (el juego continúa hasta que un cartón gane o se escriba "salir")