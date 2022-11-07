from DigrafoSecuencial import DigrafoSecuencial

if __name__ == "__main__":
    unDigrafo = DigrafoSecuencial(7, [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 0, 5), (3, 4, 6), (5, 4, 2), (5, 6, 1), (0, 4, 5), (4,5,3)])
    # print(unDigrafo.camino(1,1))
    # print(unDigrafo.adyacentes(0))
    # print(unDigrafo.get_arco(1,1))
    # print(unDigrafo.get_arco(0,1))
    # print(unDigrafo.get_arco(0,2))
    # print(unDigrafo.get_arco(0,3))
    print(unDigrafo.camino_mas_corto(0, 5))
    print(unDigrafo)
    print("\n\n")