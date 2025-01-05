import numpy as np
from utils import measure_execution_time
from algoritmos.quicksort import quicksort
from algoritmos.heapsort import heapsort
from algoritmos.shellsort import shellsort

def generate_worst_case_quicksort(n):
    """
    Gera o pior caso para o algoritmo Quicksort: uma lista ordenada de forma decrescente.
    """
    return list(range(n, 0, -1))

def generate_worst_case_heapsort(n):
    """
    Gera o pior caso para o algoritmo Heapsort: similar ao Quicksort, uma lista ordenada de forma decrescente.
    """
    return list(range(n, 0, -1))

def generate_worst_case_shellsort(n):
    """
    Gera o pior caso para o algoritmo Shellsort. Não há um consenso claro, mas listas com padrões específicos 
    podem ser usadas. Aqui utilizamos uma sequência quase ordenada com alguns elementos fora de lugar.
    """
    data = list(range(n))
    for i in range(0, len(data), 5):
        if i + 1 < n:
            data[i], data[i + 1] = data[i + 1], data[i]
    return data

def test_worst_case():
    sizes = [100, 500, 1000, 5000]  # Tamanhos dos dados para o pior caso

    for n in sizes:
        print(f"\nTamanho do vetor: {n}")
        
        # Pior caso para Quicksort
        data = generate_worst_case_quicksort(n)
        time, _ = measure_execution_time(quicksort, data)
        print(f"Pior caso - Quicksort: Tempo = {time:.6f} segundos")
        
        # Pior caso para Heapsort
        data = generate_worst_case_heapsort(n)
        time, _ = measure_execution_time(heapsort, data)
        print(f"Pior caso - Heapsort: Tempo = {time:.6f} segundos")
        
        # Pior caso para Shellsort
        data = generate_worst_case_shellsort(n)
        time, _ = measure_execution_time(shellsort, data)
        print(f"Pior caso - Shellsort: Tempo = {time:.6f} segundos")

if __name__ == "__main__":
    test_worst_case()
