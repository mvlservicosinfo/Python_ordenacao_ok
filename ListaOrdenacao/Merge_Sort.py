def aux_merge_sort(lista):

    # Merge Sort

    if len(lista) > 1:
        min = len(lista) // 2
        esquerda = lista[:min]
        direita = lista[min:]

        aux_merge_sort(esquerda)
        aux_merge_sort(direita)

        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i = i + 1
            else:
                lista[k] = direita[j]
                j = j + 1
            k = k + 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
            print(f"Merge , {lista}")
    return lista

class MergeSort(object):
    def __init__(self, lista):
        self.lista = lista

    def mergeSort(self):
        aux_merge_sort(self.lista)

