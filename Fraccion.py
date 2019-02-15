'''
Created on 17 ene. 2019

@author: d18sisaj
'''

class Fraccion:
    def __init__(self, den, num ):
        self.denominador=den;
        self.numerador=num;
    
    def fraccionVista(self):
        print(self.numerador,"/",self.denominador)
        
    def getValues(self):
        print("El valor del numerador es:" ,self.numerador," y el del denominador: ", self.denominador )
        
    def setValues(self,den,num):
        if den!=0:
            print("0 no es un denominador valido, el numerador se guardará efectivamente  pero el denominador no.")
        else:
            self.denominador=den
        self.numerador=num
    
    def valorReal(self):
        return (self.numerador/self.denominador)
    
    def multiplicar(self,mul):
        self.numerador*=mul
        
    def sumar(self, sum):
        if(self.denominador==sum.denominador):
            self.numerador+=sum.numerador
        else:
            sum.numerador*=self.denominador
            self.numerador*=sum.denominador
            self.denominador+=sum.denominador
            self.numerador+=sum.numerador
    
    def restar(self, sum):
        if(self.denomidor==sum.denominador):
            self.numerador-=sum.numerador
        else:
            sum.numerador*=self.denominador
            self.numerador*=sum.denominador
            self.denominador-=sum.denominador
            self.numerador-=sum.numerador 
            
    def multiplicarFrac(self, mul):
        self.numerador*=mul.numerador
        self.denominador*mul.denominador
    
    def simplificar(self):
        aux1=self.numerador
        
        i=0
        while(i<aux1/2):
            i+=1
            while():
                if(self.numerador%i==0 & self.denominador==0):
                    self.numerador= self.numerador/i
                    self.denominador= self.denominador/i
                else:
                    break
        self.getValues
