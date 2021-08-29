def main():
    # escribe tu código abajo de esta línea
    #GameStore tiene venta de videojuegos los nuevos tienen un costo de 1,000 y los usados 350. 
    #Escribe un programa que sirva para calcular el total de la compra. 

    nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    viejos = int(input("Dame la cantidad de juegos usados: "))
    #Proceso a hacer las operaciones correspondientes
    total = (nuevos * 1000) + (viejos * 350)
    print("El total de la compra es:", total)



if __name__ == '__main__':
    main()
