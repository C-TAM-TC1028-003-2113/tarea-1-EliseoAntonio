def main():
    # Una editorial cobra 60 dólares por página publicada y hace un 
    # descuento de 10% a los autores. Además, la editorial tiene una 
    # política que indica que 475 palabras es una página. Realiza un
    # programa que indique cuál es el costo de una publicación a 
    # partir de las palabras de la misma. Considera que se necesita 
    # una página completa aunque el número de palabras sea menor a 475.

    Npaginas = int(input("Dame el número de palabras: "))
    # Operaciones
    div1 = int(Npaginas / 475)
    div2 = int(Npaginas % 475)
    if div2 > 0:
        div1 = div1 + 1
        div1 = div1 * 60
        desc = div1 / 10
        tot = div1 - desc
        print("El costo de la publicación es:", tot)
    else:
        div1 = div1 * 60
        desc = div1 / 10
        tot = div1 - desc
        print("El costo de la publicación es:", tot)

if __name__ == '__main__':
    main()

