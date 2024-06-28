class InsertionSort:
    def __init__(self, lista):
        self.lista = lista

    def insert_sort(self):
        # comeca do segundo (indice 1 ) e vai o ultimo elemento
        for i in range(1, len(self.lista)):
            chave = self.lista[i]  # Guarda o elemento atual
            j = i - 1  # O indice do elemnto anterior
            # move os elementos da lista que são maiores que a chave para uma posição
            # a frente da sua posição atual
            while j >= 0 and chave < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
                print(f"Movimentação: {self.lista}")
            # coloca a chave na posição correta
            self.lista[j + 1] = chave
        print(f"Inserção: {i}: {self.lista}")
        return self.lista
