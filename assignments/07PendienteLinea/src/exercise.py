def main():
    # inicio pidiendo los datos como en el formato
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    # ahora que tengo los datos hare la operacion
    m = (y2 - y1) / (x2 - x1)
    #ya guarde el resultado en una variable para no perderlo, ahora es mmento de dar el resultado
    print("Pendiente:", m)

if __name__ == '__main__':
    main()
