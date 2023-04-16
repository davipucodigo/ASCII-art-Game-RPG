fps = 0.4
loops = False

## Player ##
hearth = 3
Moedas = 10
index = 0
## Inventary ##
Espada = False
Carne = False
Chave = False

def bar():
    print("\33[41m Vida: ",hearth,"\33[0m ",end=" ")
    print("\33[41m Moedas: ",str(Moedas),"\33[0m ", end=" ")
    print("\33[41m Inventario: \33[0m")
    if (Espada == True):
        print("                             Espada")
    if (Carne == True):
        print("                             Carne")
    if (Chave == True):
        print("                             Chave")
