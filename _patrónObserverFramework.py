from rx import Observable

# Crear un observable de una lista
observable = Observable.from_([1, 2, 3, 4, 5])

# Aplicar operadores a la secuencia
result = (
    observable
    .filter(lambda x: x % 2 == 0)  # Filtrar números pares
    .map(lambda x: x * 2)          # Multiplicar por 2
    .take(3)                        # Tomar solo los primeros 3 elementos
)

# Suscribirse e imprimir los resultados
result.subscribe(
    on_next=lambda value: print(f'Valor: {value}'),
    on_completed=lambda: print('Completado')
)
