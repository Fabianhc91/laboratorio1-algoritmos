"""
Ejercicio 3: Problema del Subarreglo Máximo
"""
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

random.seed(42)

# ═══════════════════════════════════════════════════════
# Arreglo personalizado (número de identificación)
# ═══════════════════════════════════════════════════════
ARREGLO = [1, -3, 1, -7, 1, -9, 5, -3, 1, -3]


# ═══════════════════════════════════════════════════════
# ALGORITMO 1: Fuerza Bruta  →  O(n²)
# ═══════════════════════════════════════════════════════
def max_subarray_bruta(arr):

    n = len(arr)
    max_suma = float('-inf')
    mejor_i, mejor_j = 0, 0

    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += arr[j]
            if suma_actual > max_suma:
                max_suma = suma_actual
                mejor_i, mejor_j = i, j

    return mejor_i, mejor_j, max_suma


# ═══════════════════════════════════════════════════════
# ALGORITMO 2: Divide y Vencerás  →  O(n log n)
# ═══════════════════════════════════════════════════════
def cruce_maximo(arr, lo, mid, hi):

    # Mejor suma desde mid hacia la izquierda
    suma_izq = float('-inf')
    suma = 0
    max_left = mid
    for i in range(mid, lo - 1, -1):
        suma += arr[i]
        if suma > suma_izq:
            suma_izq = suma
            max_left = i

    # Mejor suma desde mid+1 hacia la derecha
    suma_der = float('-inf')
    suma = 0
    max_right = mid + 1
    for j in range(mid + 1, hi + 1):
        suma += arr[j]
        if suma > suma_der:
            suma_der = suma
            max_right = j

    return max_left, max_right, suma_izq + suma_der


def max_subarray_divide(arr, lo, hi):

    # Caso base: un solo elemento
    if lo == hi:
        return lo, hi, arr[lo]

    mid = (lo + hi) // 2

    # Caso 1: mitad izquierda
    li, lj, l_suma = max_subarray_divide(arr, lo, mid)
    # Caso 2: mitad derecha
    ri, rj, r_suma = max_subarray_divide(arr, mid + 1, hi)
    # Caso 3: cruce
    ci, cj, c_suma = cruce_maximo(arr, lo, mid, hi)

    # Retornar el mayor de los tres casos
    if l_suma >= r_suma and l_suma >= c_suma:
        return li, lj, l_suma
    elif r_suma >= l_suma and r_suma >= c_suma:
        return ri, rj, r_suma
    else:
        return ci, cj, c_suma


# ═══════════════════════════════════════════════════════
# Medición de tiempos
# ═══════════════════════════════════════════════════════
def medir_tiempos(tamanios, repeticiones=10):
    tiempos_bruta  = []
    tiempos_divide = []

    for n in tamanios:
        tb, td = [], []
        for _ in range(repeticiones):
            arr = [random.randint(-100, 100) for _ in range(n)]

            t0 = time.perf_counter()
            max_subarray_bruta(arr)
            tb.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            max_subarray_divide(arr, 0, n - 1)
            td.append(time.perf_counter() - t0)

        tiempos_bruta.append(np.mean(tb) * 1000)
        tiempos_divide.append(np.mean(td) * 1000)

    return tiempos_bruta, tiempos_divide


# ═══════════════════════════════════════════════════════
# Gráfica comparativa
# ═══════════════════════════════════════════════════════
def graficar(tamanios, t_bruta, t_divide):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(tamanios, t_bruta,  marker='o', linewidth=2,
            color='#D85A30', label='Fuerza Bruta  O(n²)')
    ax.plot(tamanios, t_divide, marker='s', linewidth=2,
            color='#185FA5', label='Divide y Vencerás  O(n log n)')

    ax.set_title('Ejercicio 3: Subarreglo Máximo\nFuerza Bruta vs Divide y Vencerás',
                 fontsize=12)
    ax.set_xlabel('Tamaño de entrada (n)', fontsize=11)
    ax.set_ylabel('Tiempo promedio (ms)',   fontsize=11)
    ax.set_xticks(tamanios)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.4)

    plt.tight_layout()
    plt.savefig('grafica_ejercicio3.png', dpi=160, bbox_inches='tight')
    plt.show()
    print("Gráfica guardada: grafica_ejercicio3.png")


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════
if __name__ == "__main__":

    # ── Verificación con arreglo del taller ──────────────
    print("=" * 55)
    print("VERIFICACIÓN CON ARREGLO DEL TALLER")
    print("=" * 55)
    print(f"Arreglo: {ARREGLO}")

    i, j, s = max_subarray_bruta(ARREGLO)
    print(f"\nFuerza Bruta:")
    print(f"  Subarreglo: A[{i}..{j}] = {ARREGLO[i:j+1]}")
    print(f"  Suma máxima: {s}")

    i, j, s = max_subarray_divide(ARREGLO, 0, len(ARREGLO) - 1)
    print(f"\nDivide y Vencerás:")
    print(f"  Subarreglo: A[{i}..{j}] = {ARREGLO[i:j+1]}")
    print(f"  Suma máxima: {s}")

    # ── Experimento de tiempos ────────────────────────────
    print("\n" + "=" * 55)
    print("EXPERIMENTO DE TIEMPOS")
    print("=" * 55)

    TAMANIOS = [10, 50, 100, 200, 500, 1000]
    print("Midiendo tiempos...")
    t_bruta, t_divide = medir_tiempos(TAMANIOS)

    print(f"\n{'n':>6} | {'Fuerza Bruta (ms)':>18} | {'Divide y Vencerás (ms)':>22}")
    print("-" * 54)
    for n, tb, td in zip(TAMANIOS, t_bruta, t_divide):
        print(f"{n:>6} | {tb:>18.4f} | {td:>22.4f}")

    graficar(TAMANIOS, t_bruta, t_divide)
