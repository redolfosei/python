
class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

        conversion = {
            'inches': 1, 'feet': 12, 'yards': 36, 'miles': 63360, 
            'kilometres': 39370, 'meters': 39.37, 'centimetres': 0.4, 
            'millimetres': 0.04
        }

        self.conversion = conversion

    def mm(self):
        return self.length * self.conversion['millimetres']

    def cm(self):
        return self.length * self.conversion['centimetres']

    def m(self):
        return self.length * self.conversion['meters']

    def km(self):
        return self.length * self.conversion['kilometres']

    def mi(self):
        return self.length * self.conversion['miles']

    def yd(self):
        return self.length * self.conversion['yards']