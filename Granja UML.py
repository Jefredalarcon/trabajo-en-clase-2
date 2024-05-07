

class Cultivo:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_produccion(self):
        return self.cantidad * self.precio_unitario


class Animal:
    def __init__(self, nombre, cantidad, precio_unitario):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_produccion(self):
        return self.cantidad * self.precio_unitario


class Produccion:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_cultivo(self, nombre):
        for cultivo in self.cultivos:
            if cultivo.nombre == nombre:
                self.cultivos.remove(cultivo)
                break

    def eliminar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)
                break

    def calcular_produccion_total(self):
        total_produccion = 0
        for cultivo in self.cultivos:
            total_produccion += cultivo.calcular_produccion()
        for animal in self.animales:
            total_produccion += animal.calcular_produccion()
        return total_produccion


class Granja:
    def __init__(self):
        self.produccion = Produccion()

    def agregar_cultivo(self, cultivo):
        self.produccion.agregar_cultivo(cultivo)

    def agregar_animal(self, animal):
        self.produccion.agregar_animal(animal)

    def eliminar_cultivo(self, nombre):
        self.produccion.eliminar_cultivo(nombre)

    def eliminar_animal(self, nombre):
        self.produccion.eliminar_animal(nombre)

    def calcular_produccion_total_granja(self):
        return self.produccion.calcular_produccion_total()


# Ejemplo de uso
if __name__ == "__main__":
    
    cultivos = []
    while True:
        nombre_cultivo = input("Ingrese el nombre del cultivo (o escriba 'fin' para terminar): ")
        if nombre_cultivo.lower() == 'fin':
            break
        cantidad_cultivo = float(input("Ingrese la cantidad de {} producidos: ".format(nombre_cultivo)))
        precio_unitario_cultivo = float(input("Ingrese el precio unitario de {}: ".format(nombre_cultivo)))
        cultivo = Cultivo(nombre_cultivo, cantidad_cultivo, precio_unitario_cultivo)
        cultivos.append(cultivo)

    
    animales = []
    while True:
        nombre_animal = input("Ingrese el nombre del animal (o escriba 'fin' para terminar): ")
        if nombre_animal.lower() == 'fin':
            break
        cantidad_animal = float(input("Ingrese la cantidad de {} producidos: ".format(nombre_animal)))
        precio_unitario_animal = float(input("Ingrese el precio unitario de {}: ".format(nombre_animal)))
        animal = Animal(nombre_animal, cantidad_animal, precio_unitario_animal)
        animales.append(animal)

    
    mi_granja = Granja()

    
    for cultivo in cultivos:
        mi_granja.agregar_cultivo(cultivo)

    for animal in animales:
        mi_granja.agregar_animal(animal)

    
    produccion_total = mi_granja.calcular_produccion_total_granja()
    print("La producción total de la granja es:", produccion_total)