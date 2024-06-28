#Bubble Sort
class ordnance_BubbleSort():
    def __init__(self, lista):
        self.lista = lista

    def BubbleSeort(self):
        n = len(self.lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
                    print(f"Troca:{self.lista}")
                    print(f"Passada: {i + 1}: {self.lista}")
        return self.lista
