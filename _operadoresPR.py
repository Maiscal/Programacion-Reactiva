# Importar las clases necesarias de RxPY
from rx import Observable
from rx.operators import map, filter, merge, debounce, take



# Creación de Observables
observable_create = Observable.create(lambda observer: observer.on_next(1))
observable_interval = Observable.interval(1000).take(5)



# Transformación y Filtrado
transformed = observable_create.pipe(
    map(lambda x: x * 2),
    filter(lambda x: x > 3)
)
result = transformed.subscribe(lambda x: print(f"Transformed: {x}"))



# Combinación de Observables
observable1 = Observable.of(1, 2, 3)
observable2 = Observable.of(4, 5, 6)
merged = merge(observable1, observable2)
result = merged.subscribe(lambda x: print(f"Merged: {x}"))



# Manipulación de Tiempo
debounced = observable_interval.pipe(debounce(500))
result = debounced.subscribe(lambda x: print(f"Debounced: {x}"))



# Manejo de Errores
observable_with_error = Observable.create(lambda observer: observer.on_error(Exception("Something went wrong")))
handled_error = observable_with_error.pipe(catch_error=lambda e, _: Observable.just(f"Caught an error: {e}"))
result = handled_error.subscribe(lambda x: print(x), lambda e: print(f"Error handled: {e}"))



# Operadores de Utilidad
observable_do_action = Observable.of(1, 2, 3)
with_side_effect = observable_do_action.pipe(do_action=lambda x: print(f"Doing something with: {x}"))
result = with_side_effect.subscribe(lambda x: print(f"With side effect: {x}"))



# Operadores de Agregación
observable_numbers = Observable.of(1, 2, 3, 4, 5)
sum_result = observable_numbers.pipe(reduce=lambda acc, x: acc + x)
result = sum_result.subscribe(lambda x: print(f"Sum: {x}"))
