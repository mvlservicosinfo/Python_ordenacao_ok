class SelectionSort(object):
    def __init__(self, lista):
        self.lista = lista

    def selection_sort(self):
        if not self.lista:
            return self.lista
        for i in range(len(self.lista)):
            min = i
            for j in range(i + 1, len(self.lista)):
                if self.lista[j] < self.lista[min]:
                    min = j
            self.lista[i], self.lista[min] = self.lista[min], self.lista[i]
            print(f"Trocado: {i+1} : {self.lista}")
        return self.lista






