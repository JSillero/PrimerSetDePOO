'''
Created on 15 ene. 2019

@author: d18sisaj
'''


class cubo:
    def __init__(self,cap):
        self.__capacidad=cap
        self.__contenido=0

        
    def getCap(self):
        return self.__capacidad
    
    def setCont(self,con):
        self.__contenido=con
        
    def vacia(self):
        self.__contenido=0
        
    def getCont(self):
        return self.__contenido
    
    def llena(self):
        self.__contenido=self.__capacidad
        
    def pinta(self):
        contenido2=self.__contenido
        capacidad2=self.__capacidad
        while capacidad2>=0:
            
            if capacidad2==0:
                print("*****")
                capacidad2-=1
            else:
                if capacidad2>contenido2:
                    print("*   *")
                    capacidad2-=1
                else:
                    if capacidad2==contenido2 & ( capacidad2!=0):
                        print("*~~~*")
                        capacidad2-=1
                        contenido2-=1
            
            
                
    def vuelcaEn(self, cubo):
        libre=cubo.getCap()-cubo.getCont()
        if libre>0:
            if(self.__contenido<=libre):
                cubo.setCont(self,(cubo.getCont(self)+self.getCont() ) )
                self.vacia()
            else:
                self.__contenido-=libre
                cubo.llena(self)
                
                
                
cubo1= cubo(8)

cubo1.pinta()
    