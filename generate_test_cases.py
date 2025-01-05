import random

def generate_test_cases(size):
    """Gera casos de teste com diferentes arranjos."""
    return {
        "crescente": list(range(size)),
        "decrescente": list(range(size, 0, -1)),
        "aleatorio": [random.randint(0, size) for _ in range(size)],
        "quase_ordenado": [x if random.random() > 0.1 else random.randint(0, size) for x in range(size)],
    }
