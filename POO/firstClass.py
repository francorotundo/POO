class Hotel:
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def añadir_huspedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes
    
    def ocupacion_total(self):
        return self.huespedes

hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
hotel.añadir_huspedes(3)
hotel.checkout(1)
print(hotel.ocupacion_total())
print(hotel.lugares_de_estacionamiento)
