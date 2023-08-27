class Control:
    def _init_(self):
        self.tv = None
    
    def turnOn(self):
        if self.tv is not None:
            self.tv.turnOn()
    def turnOff(self):
        if self.tv is not None:
            self.tv.turnOff()
    
    def canalUp(self):
        if self.tv is not None:
            self.tv.canalUp()
    def canalDown(self):
        if self.tv is not None:
            self.tv.canalDown()
    
    def volumeDown(self):
        if self.tv is not None:
            self.tv.canalDown()
    def volumeUp(self):}
        if self.tv is not None:
            self.tv.volumenUp()
    
    def setCanal(self,canal):
        if self.tv is not None:
            self.tv.setCanal()
    def setVolumen(self, volumen):
        if self.tv is not None:
            self.tv.setVolumen()
    
    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)