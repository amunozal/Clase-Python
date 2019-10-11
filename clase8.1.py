class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)
#y ahora queremos anador una clase Cirulo que herede de punto. Para conocer todos los detalles
class Circulo(Punto):
    def __init__(self, radio, *args, **kwargs):
        self.radio = radio
        super().__init__(*args, **kwarg)
    def __repr__(self):
        return "x: {}, y: {}, radio: {}".format(self.x, self.y, self.radio)