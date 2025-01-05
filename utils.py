import time
import numpy as np
from scipy.optimize import curve_fit

def measure_execution_time(func, data):
    """
    Mede o tempo de execução de uma função de ordenação.
    
    Args:
        func (callable): Função de ordenação.
        data (list): Lista de entrada para a ordenação.
        
    Returns:
        tuple: Tempo de execução em segundos e o resultado da ordenação.
    """
    start_time = time.perf_counter()
    result = func(data)
    end_time = time.perf_counter()
    return end_time - start_time, result

def complexity_nlogn(n, a):
    """
    Função de complexidade O(n log n).
    
    Args:
        n (array-like): Tamanhos de entrada.
        a (float): Constante de proporcionalidade.
        
    Returns:
        array-like: Valores calculados para a complexidade.
    """
    return a * n * np.log2(n)

def complexity_n2(n, a):
    """
    Função de complexidade O(n^2).
    
    Args:
        n (array-like): Tamanhos de entrada.
        a (float): Constante de proporcionalidade.
        
    Returns:
        array-like: Valores calculados para a complexidade.
    """
    return a * n ** 2

def analyze_complexity(sizes, times, complexity_func):
    """
    Ajusta uma curva de complexidade e imprime a constante associada.
    
    Args:
        sizes (list): Tamanhos das entradas testadas.
        times (list): Tempos medidos.
        complexity_func (callable): Função de complexidade (ex: O(n log n)).
    """
    sizes = np.array(sizes)
    times = np.array(times)
    
    # Ajuste da curva
    popt, _ = curve_fit(complexity_func, sizes, times)
    a = popt[0]
    
    print(f"Constante ajustada para {complexity_func.__name__}: a = {a:.6f}")
    return a
