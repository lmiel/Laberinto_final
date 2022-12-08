import laberinto_code as lab

if __name__=="__main__":
    laberinto = lab.laberinto(lab.muro)
    for i in range(0,lab.altura):
        print(laberinto[i])
    print(lab.resolver(laberinto))
