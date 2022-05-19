#Clase sin getter and setter

class Millas:
	def __init__(self, distancia = 0):
		self._distancia = distancia

	def convertir_a_kilometros(self):
		return (self._distancia * 1.609344)

#Utilizando getters and setters

    # Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor
    
if __name__=='__main__':
    # Creamos un nuevo objeto
    avion = Millas()

    # Indicamos la distancia
    avion._distancia = 200

    # Obtenemos el atributo distancia
    print(avion.distancia)

    # Obtenemos el método convertir_a_kilometros
    print(avion.convertir_a_kilometros())