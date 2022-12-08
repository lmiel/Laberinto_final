# Laberinto
LINK REPOSITORIO: https://github.com/lmiel/Laberinto_final.git
________________________________________________________________________________________________________________________________________
TAREA II:
La segunda tarea a resolver consiste en construir un programa para recorrer el laberinto desde la entrada a la salida. La entrada siempre está en la esquina superior izquierda y la salida en la esquina inferior derecha.

El programa debe devolver una lista con la secuencia de movimientos para ir de la entrada a la salida del laberinto, tal y como se muestra a continuación:

['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha',
________________________________________________________________________________________________________________________________________

TAREA I
La primera tarea consiste en construir un laberinto como el de la siguiente figura.

Laberinto

El laberinto se representará como una una lista de listas, donde cada lista es una fila del laberinto y cada casilla se representará con un espacio ' ' si hay paso o con la letra ‘X’ si hay un muro, tal y como se muestra a continuación:

laberinto = [
    [' ', 'X', 'X', 'X', 'X'],
    
    [' ', 'X', ' ', ' ', ' '],
    
    [' ', 'X', ' ', 'X', ' '], 
    
    [' ', ' ', ' ', 'X', ' '], 
    
    ['X', 'X', 'X', 'X', 'S']
    
El laberinto se debe crear a partir de una tupla con las coordenadas de las casillas donde hay muro, como la siguiente:

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
