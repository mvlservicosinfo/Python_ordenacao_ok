import random


class ordnance_BubbleSort():
    def __init__(self, lista):
        self.lista = lista

    def __get_lista(self):
        return self.lista

    def __set_lista(self, lista):
        self.lista = lista

    def BubbleSeort(self):
        lista = self.__get_lista()
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    print(f"Troca:{lista}")
                    print(f"Passada: {i + 1}: {lista}")
        return lista
