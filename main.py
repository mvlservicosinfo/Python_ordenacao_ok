import random

from ListaOrdenacao.BubbleSort import ordnance_BubbleSort
from ListaOrdenacao.InsertSort import InsertionSort

if __name__ == '__main__':

    op = int(input(f"Digite a Opção: "))
    lp = random.sample(range(100), 10)

    if op==1:
        b = ordnance_BubbleSort(lp)
        print("\nLista ordenada por Bubble Sort: ")
        print(b.BubbleSeort())
    elif op==2:
        c = InsertionSort(lp)
        print("\nLista ordenada por Insertion Sort: ")
        print(c.insert_sort())

