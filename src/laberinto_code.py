altura = 5
ancho = 5
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def laberinto(muro):
    laberinto = [] #crea una lista vacia
    #Queremos crear un bucle que recorra la matriz bloque por bloque, en este caso de izquierda a derecha y bajando fila por fila
    for x in range(0,altura): #bucle que recorre la matriz por fila
        fila=[]
        for y in range(0,ancho): #bucle que recorre la matriz por columna
            tupla=(x,y)
            if tupla == (0,0):
                fila.append('E')
            elif tupla in muro:
                fila.append("X")
            else:
                fila.append(' ') 
        if x == altura - 1 and y == ancho - 1:
            fila.pop()
            fila.append('S')
        laberinto.append(fila)
    return laberinto

def resolver(laberinto):
    movimientos = []
    posicionx = 0
    posiciony = 0
    posantx = 0
    posanty = 0
    while posicionx != ancho - 1 or posiciony != altura - 1:
        if posiciony + 1 < ancho and laberinto[posicionx][posiciony + 1] in (" ","S") and posanty != posiciony + 1 :
            movimientos.append("derecha")
            posanty = posiciony
            posantx = posicionx
            posiciony = posiciony + 1
        elif posicionx + 1 < altura and laberinto[posicionx + 1][posiciony] in (" ","S") and posantx != posicionx + 1:
            movimientos.append("abajo")
            posantx = posicionx
            posanty = posiciony
            posicionx = posicionx + 1
        elif posiciony - 1 < ancho and laberinto[posicionx][posiciony - 1] == " " and posanty != posiciony - 1:
            movimientos.append("izquierda")
            posanty = posiciony
            posantx = posicionx
            posiciony = posiciony - 1
        elif posicionx - 1 < ancho and laberinto[posicionx - 1][posiciony] == " " and posantx != posicionx - 1 :
            movimientos.append("arriba")
            posantx = posicionx
            posanty = posiciony
            posicionx = posicionx - 1
    return movimientos


