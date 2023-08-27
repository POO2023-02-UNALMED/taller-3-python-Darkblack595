from televisores.tv import TV
class Control:
    def __init__(self, tv):
        TV.tv = self.tv
    
    def turnOn(self):
            self.tv.turnOn()
    def turnOff(self):
            self.tv.turnOff()
    
    def canalUp(self):
            self.tv.canalUp()
    def canalDown(self):
            self.tv.canalDown()
    
    def volumeDown(self):
            self.tv.canalDown()
    def volumeUp(self):
            self.tv.volumenUp()
    
    def setCanal(self,canal):
            self.tv.setCanal()
    def setVolumen(self, volumen):
            self.tv.setVolumen()
    
    def enlazar(self, tv):
        self.tv = tv
        TV.tv.setControl(self)