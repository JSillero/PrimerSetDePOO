'''
Created on 17 ene. 2019

@author: d18sisaj
'''

class Fraccion:
    def __init__(self, den, num ):
        self.denominador=den;
        self.__numerador=num;
    
    def fraccionVista(self):
        print(self.__numerador,"/",self.denominador)
        
    def getValues(self):
        print("El valor del __numerador es:" ,self.__numerador," y el del denominador: ", self.denominador )
        
    def setValues(self,den,num):
        if den!=0:
            print("0 no es un denominador valido, el __numerador se guardará efectivamente  pero el denominador no.")
        else:
            self.denominador=den
        self.__numerador=num
    
    def valorReal(self):
        return (self.__numerador/self.denominador)
    
    def multiplicar(self,mul):
        self.__numerador+=mul*self.denominador
        
    def sumar(self, sum):
        if(self.denominador==sum.denominador):
            self.__numerador+=sum.__numerador
        else:
            sum.__numerador*=self.denominador
            self.__numerador*=sum.denominador
            self.denominador+=sum.denominador
            self.__numerador+=sum.__numerador
    
    def restar(self, sum):
        if(self.denominador==sum.denominador):
            self.__numerador-=sum.__numerador
        else:
            sum.__numerador*=self.denominador
            self.__numerador*=sum.denominador
            self.denominador-=sum.denominador
            self.__numerador-=sum.__numerador 
            
    def multiplicarFrac(self, mul):
        self.__numerador*=mul.__numerador
        self.denominador*mul.denominador
    
    def simplificar(self):
        aux1=self.__numerador
        
        i=1
        while(i<aux1/2):
            i
            while():
                if(self.__numerador%i==0 & self.denominador%i==0):
                    self.__numerador= self.__numerador/i
                    self.denominador= self.denominador/i
                else:
                    break
        
