class person:
    def __init__(self,name,age,cllgname):
        self.myname=name
        self.age=age
        self.cllgname=cllgname

    def mycllg(self):
        print("my cllg name is"+self.myname)

hari=person("hari",22,"kiot") 
hari.mycllg()       

