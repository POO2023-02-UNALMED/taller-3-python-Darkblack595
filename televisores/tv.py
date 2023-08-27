class TV:
    numTV = 0
    def __init__(self , marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = None
        TV.numTV += 1

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def getMarca (self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    
    def getVolumen (self):
        return self.volumen
    def setVolumen(self, volumen):
        if self.estado == True and self.volumen >=0 and self.volumen <= 7:
            self.volumen = volumen
    
    def getCanal (self):
        return self.canal
    def setCanal(self, canal):
        if self.estado == True and self.canal >=1 and self.canal <= 120:
            self.canal = canal
    
    def getPrecio (self):
        return self.precio
    def setPrecio (self, precio):
        self.precio = precio
    
    def getControl(self):
        return self.control
    def setControl(self,control):
        self.control = control
    
    def getEstado (self):
        return self.estado    
   
    @classmethod
    def getNumTV (cls):
        return cls.numTV
    def setNumTV(numTV):
        TV.numTV = numTV

    def canalUp(self):
        self.setCanal(self.getCanal() + 1)
    def canalDown(self):
        self.setCanal(self.getCanal() + 1)

    def volumenUp(self):
        self.setVolumen(self.getVolumen() + 1)
    def volumenDown(self):
        self.setVolumen(self.getVolumen() - 1)
    
