"""
Ejercicio 4: Comparación Merge Sort vs Insertion Sort
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
ARREGLO = [1, 3, 1, 7, 1, 9, 5, 3, 1, 3]


# ═══════════════════════════════════════════════════════
# MERGE SORT  →  O(n log n)
# ═══════════════════════════════════════════════════════
def mezclar(izq, der):
    """
    Mezcla dos arreglos ordenados en uno solo ordenado.
    """
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def merge_sort(arr):
    """
    Merge Sort recursivo.
    
    """
    if len(arr) <= 1:
        return arr[:]  # Caso base

    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha   = merge_sort(arr[mid:])

    return mezclar(izquierda, derecha)


# ═══════════════════════════════════════════════════════
# INSERTION SORT  →  O(n²)
# ═══════════════════════════════════════════════════════
def insertion_sort(arr):
    """
    Insertion Sort iterativo.
    
    """
    arr = arr[:]  # Copiar para no modificar el original

    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1

        # Mover elementos mayores que 'clave' una posición adelante
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = clave

    return arr


# ═══════════════════════════════════════════════════════
# Medición de tiempos
# ═══════════════════════════════════════════════════════
def medir_tiempos(tamanios, repeticiones=10):
    tiempos_ms = []
    tiempos_is = []

    for n in tamanios:
        tms, tis = [], []
        for _ in range(repeticiones):
            arr = [random.randint(-1000, 1000) for _ in range(n)]

            t0 = time.perf_counter()
            merge_sort(arr)
            tms.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            insertion_sort(arr)
            tis.append(time.perf_counter() - t0)

        tiempos_ms.append(np.mean(tms) * 1000)
        tiempos_is.append(np.mean(tis) * 1000)

    return tiempos_ms, tiempos_is


# ═══════════════════════════════════════════════════════
# Gráfica comparativa
# ═══════════════════════════════════════════════════════
def graficar(tamanios, t_ms, t_is):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(tamanios, t_ms, marker='s', linewidth=2,
            color='#185FA5', label='Merge Sort  O(n log n)')
    ax.plot(tamanios, t_is, marker='o', linewidth=2,
            color='#D85A30', label='Insertion Sort  O(n²)')

    ax.set_title('Ejercicio 4: Merge Sort vs Insertion Sort',
                 fontsize=12)
    ax.set_xlabel('Tamaño de entrada (n)', fontsize=11)
    ax.set_ylabel('Tiempo promedio (ms)',  fontsize=11)
    ax.set_xticks(tamanios)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.4)

    plt.tight_layout()
    plt.savefig('grafica_ejercicio4.png', dpi=160, bbox_inches='tight')
    plt.show()
    print("Gráfica guardada: grafica_ejercicio4.png")


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════
if __name__ == "__main__":

    # ── Verificación con arreglo del taller ──────────────
    print("=" * 55)
    print("VERIFICACIÓN CON ARREGLO DEL TALLER")
    print("=" * 55)
    print(f"Arreglo original: {ARREGLO}")

    resultado_ms = merge_sort(ARREGLO)
    print(f"\nMerge Sort:")
    print(f"  Resultado: {resultado_ms}")

    resultado_is = insertion_sort(ARREGLO)
    print(f"\nInsertion Sort:")
    print(f"  Resultado: {resultado_is}")

    # Verificar que ambos dan el mismo resultado
    if resultado_ms == resultado_is:
        print("\n✓ Ambos algoritmos producen el mismo resultado ordenado")
    else:
        print("\n✗ ERROR: Los resultados no coinciden")

    # ── Experimento de tiempos ────────────────────────────
    print("\n" + "=" * 55)
    print("EXPERIMENTO DE TIEMPOS")
    print("=" * 55)

    TAMANIOS = [10, 50, 100, 500, 1000, 5000]
    print("Midiendo tiempos...")
    t_ms, t_is = medir_tiempos(TAMANIOS)

    print(f"\n{'n':>6} | {'Merge Sort (ms)':>16} | {'Insertion Sort (ms)':>20}")
    print("-" * 50)
    for n, tm, ti in zip(TAMANIOS, t_ms, t_is):
        print(f"{n:>6} | {tm:>16.4f} | {ti:>20.4f}")

    graficar(TAMANIOS, t_ms, t_is)
