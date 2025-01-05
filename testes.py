import matplotlib.pyplot as plt
from generate_test_cases import generate_test_cases
from utils import measure_execution_time
from algoritmos.quicksort import quicksort
from algoritmos.heapsort import heapsort
from algoritmos.shellsort import shellsort

# Tamanhos dos vetores a serem testados
sizes = [100, 500, 1000, 5000]

# Tipos de testes
test_cases = ["crescente", "decrescente", "aleatorio", "quase_ordenado"]

# Funções de ordenação a serem testadas
sorting_algorithms = {
    "Quicksort": quicksort,
    "Heapsort": heapsort,
    "Shellsort": shellsort,
}

# Resultados por caso de teste
test_results_by_case = {case: {} for case in test_cases}

# Executar os testes
for case in test_cases:
    print(f"Executando testes para caso: {case}")
    for name, algorithm in sorting_algorithms.items():
        print(f"  Testando algoritmo: {name}")
        execution_times = []
        for size in sizes:
            test_data = generate_test_cases(size)[case]
            time_taken, _ = measure_execution_time(algorithm, test_data)
            execution_times.append(time_taken)
        test_results_by_case[case][name] = execution_times

# Gerar gráficos para cada caso de teste
def plot_results_by_case(test_results_by_case):
    for case, results in test_results_by_case.items():
        plt.figure(figsize=(10, 6))
        plt.title(f"Comparação de Algoritmos - Caso: {case}")
        plt.xlabel("Tamanho do vetor")
        plt.ylabel("Tempo de execução (segundos)")

        for name, times in results.items():
            plt.plot(sizes, times, label=name, marker='o')

        plt.legend()
        plt.grid(True)
        plt.savefig(f"grafico_{case}.png")
        plt.show()

plot_results_by_case(test_results_by_case)
