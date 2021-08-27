def main():
    # Pedire los datos necesarios
    mens = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minu = int(input("Dame el numero de minutos: "))
    # hare las operaciones necesarias
    suma = (mens + megas + minu)* 0.80
    #Dare el resultado 
    print("El costo mensual es:", suma)


if __name__ == '__main__':
    main()
