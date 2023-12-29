# Interfaz del Observador
class Observador:
    def actualizar(self):
        pass

# Sujeto
class Sujeto:
    def __init__(self):
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar()

# Observador Concreto
class ObservadorConcreto(Observador):
    def actualizar(self):
        print("El estado del sujeto ha cambiado.")

# Uso del patrón Observer
sujeto = Sujeto()
observador1 = ObservadorConcreto()
observador2 = ObservadorConcreto()

sujeto.registrar_observador(observador1)
sujeto.registrar_observador(observador2)

sujeto.notificar_observadores()
