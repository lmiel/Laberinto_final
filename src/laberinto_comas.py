altura = 5
ancho = 5

def laberinto():
    muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
    laberinto = [] #crea una lista vacia
    #Queremos crear un bucle que recorra la matriz bloque por bloque, en este caso de izquierda a derecha y bajando fila por fila
    for x in range(0,altura): #bucle que recorre la matriz por fila
        fila=[]
        for y in range(0,ancho): #bucle que recorre la matriz por columna
            tupla=(x,y)
            if tupla in muro:
                fila.append("X")
            else:
                fila.append(' ') 
        if x == altura - 1 and y == ancho - 1:
            fila.pop()
            fila.append('S')
        laberinto.append(fila)
    return laberinto

if __name__=="__main__":
    for y in range(0,altura):
        print(laberinto()[y])

