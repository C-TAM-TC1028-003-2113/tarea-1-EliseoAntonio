def main():
    # Se requieren 50 gramos de levadura para 1 kg. 
    # de harina si se utiliza para la base de una pizza. 
    # Realiza el cálculo de la levadura necesitada a 
    # partir de los gramos de harina que indique el usuario.
     
    gramosA = float(input("Dame la harina en gramos: "))
    #Operaciones, 1 gramo de levadura es igual a 20 de harina.
    div1 = gramosA / 20
    #Salida
    print("Necesitas estos gramos de levadura:", div1)
   
if __name__ == '__main__':
    main()
