# Quick sort
def quick_sort(lista):
    # Funcao Auxiliar para realizar a prticao
    def particao(lista, baixo, alto):
        # Pivo e o ultimo elemento
        pivo = lista[alto]
        i = baixo - 1
        # Percorre a lista do indice do menor elemento
        # até o indice do pivo
        for j in range(baixo, alto):
            if lista[j] <= pivo:
                i += 1
                # troca os elementos
                lista[i], lista[j] = lista[j], lista[i]
                # troca o pivo para posicao correta
        lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
        return i + 1

    # Funcao Recursiva principal do quick sort
    def quick_sort_recursiva(lista, baixo, alto):
        if baixo < alto:
            # Indice da Particao
            p = particao(lista, baixo, alto)
            # Ordena os elementos antes e depois da particao
            quick_sort_recursiva(lista, baixo, p - 1)
            quick_sort_recursiva(lista, p + 1, alto)

    # Chamada inicial da funcao recursiva
    quick_sort_recursiva(lista, 0, len(lista) - 1)
    return lista
class Quick_Sort(object):
    def __init__(self, lista):
        self.lista = lista

    def quick_sort(self):
        return quick_sort(self.lista)
