class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}')

    def _añadir_jabon(self):
        print(f'Añadiendo jabón')
    
    def _lavar(self):
        print(f'Lavando la ropa')
    
    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__=='__main__':
    lavadora=Lavadora()
    lavadora.lavar()