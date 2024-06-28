import random

from ListaOrdenacao.BubbleSort import ordenance_BubbleSort
from ListaOrdenacao.InsertSort import InsertionSort
from ListaOrdenacao.Merge_Sort import MergeSort
from ListaOrdenacao.QuickSort import Quick_Sort
from ListaOrdenacao.SelectionSort import SelectionSort

if __name__ == '__main__':
    try:
        op = int(input(f"Digite a Opção: "))
        lp = random.sample(range(100), 10)

        if op == 1:
            b = ordenance_BubbleSort(lp)
            print("\nLista ordenada por Bubble Sort: ")
            print(b.BubbleSeort())
        elif op == 2:
            c = InsertionSort(lp)
            print("\nLista ordenada por Insertion Sort: ")
            print(c.insert_sort())
        elif op == 3:
            d = SelectionSort(lp)
            print("\nLista ordenada por Selection Sort: ")
            print(d.selection_sort())
        elif op == 4:
            e = MergeSort(lp)
            print("\nLista ordenada por Merge Sort: ")
            print(e.mergeSort())
        elif op == 5:
            f = Quick_Sort(lp)
            print("\nLista ordenada por Quick Sort: ")
            print(f.quick_sort())
    except ValueError:
        print("Opção Não Encontrada!")


