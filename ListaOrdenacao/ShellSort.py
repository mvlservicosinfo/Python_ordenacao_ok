class shell_Sort(object):

    def __init__(self, lista):
        self.lista = lista

    # Shell sort

    def shell_sort(self):
        n = len(self.lista)
        intervalo = n // 2
        # Dividindo o intervalo ate que saja igual a Zero
        while intervalo > 0:
            # Percorre a lista
            for i in range(intervalo, n):
                temp = self.lista[i]
                j = i
                while j >= intervalo and self.lista[j - intervalo] > temp:
                    self.lista[j] = self.lista[j - intervalo]
                    j -= intervalo
                    # inserir o valor guardado na posicao correta
                    self.lista[j] = temp
                    # exibir a lista apos cada reducao de intervalo
            print(f"Intervalo {intervalo} : {self.lista}")
            intervalo //= 2
        return self.lista
