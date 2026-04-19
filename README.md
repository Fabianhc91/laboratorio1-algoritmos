# Laboratorio 1 - Análisis de Algoritmos

**Estudiante:** Fabian Hincapié Castañeda  
**Institución:** Instituto Tecnológico Metropolitano - ITM  
**Fecha:** Abril 2026

## Contenido

### Ejercicio 3: Problema del Subarreglo Máximo
- `ejercicio3_subarreglo_maximo.py` - Fuerza bruta y divide y vencerás
- `grafica_ejercicio3.png` - Comparación de tiempos

### Ejercicio 4: Merge Sort vs Insertion Sort
- `ejercicio4_merge_vs_insertion.py` - Implementación
- `grafica_ejercicio4.png` - Comparación de tiempos

## Cómo ejecutar

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install matplotlib seaborn numpy
python ejercicio3_subarreglo_maximo.py
python ejercicio4_merge_vs_insertion.py
```

## Resultados

- Divide y vencerás: **20× más rápido** (n=1000)
- Merge Sort: **48× más rápido** (n=5000)
