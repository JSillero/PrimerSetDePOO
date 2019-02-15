'''
Created on 15 ene. 2019

@author: d18sisaj
'''
class gato_simple:
    
    def __init__(self,s):
        
        self.sexo=s
        
    def getSex(self):
        return self.sexo
    
    def maullar(self):
        print("Miauuuuuuuuuuuuuuuuuuuuuuuuuuu :3")
    def ronronea(self):
        print("Prrrrrrrrrrrrr =3")
    
    def comer (self, comida):
        if(comida=="pescado"):
            print("Muy rico muchas gracias nya")
        else:
            print("Solo como pescado >:3")
    def pelear(self,gato):
        '''El comportamiento de este programa no refleja las opiniones o puntos de vista del programador 
        de ninguna manera, el responsable es la autoridad que mando la creacion del mismo'''
        
        if(self.sexo=="hembra"):
            print("No me gusta pelear =3")
        else:
            if(gato.getSex()=="hembra"):
                print("No peleo con gatitas :3c")
            else:
                print("Te voy a undir el pesho >:3")

gatoh= gato_simple("hembra")
gatom= gato_simple("macho")
gatom2= gato_simple("macho")

gatoh.pelear(gatom)
gatom.pelear(gatoh)
gatom.pelear(gatom2)

gatom.ronronea()
gatoh.maullar()

gatoh.comer("pescado")
gatoh.comer("otra cosa")

