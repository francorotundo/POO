class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Estoy caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'Estoy moviendome en mi bicicleta.')

if __name__=='__main__':
    persona = Persona('Franco')
    persona.avanza()

    ciclista = Ciclista('Rixy')
    ciclista.avanza()