'''
Created on 16 ene. 2019

@author: d18sisaj
'''


class Cuadrado:
    def __init__(self,l):
        self.__lado=l
        
    def toString(self):
        resultado=""
       
        i=0
        while(i<(self.__lado+2)):
            i+=1
            resultado+="*"
        
        resultado+="\n"
        
        
        i=1
        while(i<(self.__lado-1)):
            i+=1
            
            resultado+="*"
            esp=0
            while(esp<self.__lado):
                resultado+=" "
                esp+=1
            resultado+="*\n"
        
        i=0
     
        while(i<(self.__lado+2)):
            i+=1
            resultado+="*"
        resultado+="\n"
        print(resultado)
        
        return resultado
    
cuadrado6= Cuadrado(10)
cuadrado6.toString()