from utils import measure_execution_time, analyze_complexity, complexity_nlogn, complexity_n2
from algoritmos.quicksort import quicksort
from algoritmos.heapsort import heapsort
from algoritmos.shellsort import shellsort
import numpy as np
import matplotlib.pyplot as plt

# Tamanhos de entrada para os testes
sizes = [100, 200, 400, 800, 1600, 3200, 6400]

# Algoritmos de ordenação para teste
algorithms = {
    "Quicksort": quicksort,
    "Heapsort": heapsort,
    "Shellsort": shellsort,
}

# Testando cada algoritmo
results = {}

for name, algorithm in algorithms.items():
    print(f"Testando {name}...")
    times = []
    for size in sizes:
        # Gerar massa de dados aleatória
        test_case = np.random.randint(0, 10000, size)
        # Medir tempo de execução
        time_taken, _ = measure_execution_time(algorithm, test_case)
        times.append(time_taken)
    results[name] = times

# Visualizando os resultados
plt.figure(figsize=(10, 6))
for name, times in results.items():
    plt.plot(sizes, times, label=name)

plt.xlabel("Tamanho da Entrada")
plt.ylabel("Tempo de Execução (s)")
plt.title("Comparação de Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.show()

# Análise de complexidade para cada algoritmo
for name, times in results.items():
    print(f"Analisando complexidade para {name}...")
    if name == "Shellsort":
        complexity_function = complexity_n2  # Estimado como O(n^2)
    else:
        complexity_function = complexity_nlogn  # Estimado como O(n log n)
    analyze_complexity(sizes, times, complexity_function)
