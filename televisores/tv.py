class TV:
    numTV = 0
    def __init__(self , marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        numTV += 1

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
    def setNumTV(cls,numTV):
        cls.estado = numTV

    def canalUp(self):
        if self.estado == True:
            self.canal = self.setCanal(self.getCanal()+1)
    def canalDown(self):
        if self.estado == True:
            self.canal = self.setCanal(self.getCanal()-1)

    def volumenUp(self):
        if self.estado == True:
            self.volumen = self.setVolumen(self.getVolumen()+1)
    def volumenDown(self):
        if self.estado == True:
            self.volumen = self.setVolumen(self.getVolumen()-1)
    
