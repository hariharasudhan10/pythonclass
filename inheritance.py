#parent class
class car:
    def sound(self,tyre,glass):
        self.tyre=tyre
        self.glass=glass
        print(self.tyre+"my glass type "+self.glass)
  #child1    
class bmw(car):
    def model(self,engine_power,ac):
        self.engine_power=engine_power
        self.ac=ac
        print(self.engine_power+" my ac type "+self.ac)
#child 2
class maruthi(bmw):
    def design(self,seat,windows):
        self.seat=seat
        self.windows=windows
        print(self.seat+" my windows type "+self.windows)
series1=maruthi()
series1.sound("speed","two ton ac")

