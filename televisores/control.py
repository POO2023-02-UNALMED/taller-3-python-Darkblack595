from tv import TV
class Control:
    def _init_(self):
        self.tv = None
    
    def turnOn(self):
        TV.turnOn()
    def turnOff(self):
        TV.turnOff()
    
    def canalUp(self):
        TV.canalUp()
    def canalDown(self):
        TV.canalDown()
    
    def volumeDown(self):
        TV.canalDown()
    def volumeUp(self):
        TV.canalUp()
    
    def setCanal(self):
        TV.setCanal()
    def setVolumen(self):
        TV.setVolumen()
    
    def enlazar(self, tv):
        self.tv = tv
        TV.setControl(self)