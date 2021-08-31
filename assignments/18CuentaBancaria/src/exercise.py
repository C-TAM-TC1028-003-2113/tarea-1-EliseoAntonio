def main():
    # Un banco cobra el 7.5% de interés mensual sobre 
    # el saldo final de una cuenta. Además, cada cheque 
    # expedido tiene un costo de 13 pesos. Realiza un 
    # programa para obtener el saldo mensual de una cuenta 
    # en este banco tomando en cuenta el saldo del mes anterior,
    # los ingresos, los egresos y el número de cheques expedidos.
    
    saldoA = float(input("Dame el saldo del mes anterior: "))
    ingre = float(input("Dame los ingresos: "))
    egre = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    #operacion
    SinI = ((saldoA + ingre) - (egre + (cheques * 13)))
    interes = SinI * 0.075
    total = SinI - interes
    #salida
    print("El saldo final de la cuenta es:", total)

if __name__ == '__main__':
    main()
