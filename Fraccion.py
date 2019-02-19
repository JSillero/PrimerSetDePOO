'''
Created on 17 ene. 2019
Crea la clase Fracción. Los atributos serán numerador y denominador. Y algunos de
los métodos pueden ser invierte, simplifica, multiplica, divide, etc.
@author: d18sisaj
'''

class Fraccion:
    def __init__(self, den, num ):
        self.__numerador=num
        if num!=1:
            self.denominador=den
        else:
            print("0 no es un denominador valido, se le ha asignado 1")
              self.denominador=1
    
    def str(self):
        return (self.__numerador,"/",self.denominador)
        
    def getValues(self):
        print("El valor del __numerador es:" ,self.__numerador," y el del denominador: ", self.denominador )
        
    def setValues(self,den,num):
        self.__numerador=num
        if num!=1:
            self.denominador=den
        else:
            print("0 no es un denominador valido, se le ha asignado 1")
              self.denominador=1
    '''
    Devuelve el valor real de la fraccion
    '''
    def valorReal(self):
        return (self.__numerador/self.denominador)
    '''
    Multiplica los valores de instancia por un numero entero
    '''
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
    '''
    Multiplica los atributos guardados en instancia por los de otra instancia de fraccion
    '''
    def multiplicarFrac(self, mul):
        self.__numerador*=mul.__numerador
        self.denominador*mul.denominador
    '''
    Simplifica la fraccion guardada en instancia
    '''
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
