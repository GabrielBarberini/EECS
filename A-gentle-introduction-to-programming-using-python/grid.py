import math

def grid(x,y):   
    n = int(math.sqrt(y**2))
    m = int(math.sqrt(x**2))

    horizontal = ("+ ") + ("- "*m)
    base = (horizontal*n) + ("+\n")

    vertical = (n+1) * ("| " + ("  "*m))
    column = (vertical + ("\n")) * n

    print((base+column) * n + base)

largura = int(input("Largura do grid: "))
coluna = int(input("Numero de colunas do grid: "))

grid(largura,coluna)
