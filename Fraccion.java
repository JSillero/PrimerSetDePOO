package ejerciciosobjetosJ;

public class Fraccion {
  private int denominador;
  private int numerador;
  
  Fraccion(int num, int den){
    this.denominador=den;
    this.numerador=num;
  }
  
  String FraccionVista() {
    return(Integer.toString(this.numerador)+"/"+Integer.toString(this.denominador));
  }
  
  void getValues() {
    System.out.println("El valor actual de numerador es:"+this.numerador +"\n Y el del denominador: "+ this.denominador );
  }
  void setValues(int num, int den ) {
    if(den!=0) 
      this.denominador=den;
    else
      System.out.println("0 no es un denominador valido, el numerador se guardará efectivamente  pero el denominador no.");;
    this.numerador=num;
  }
  float valorReal() {
    return (this.numerador/this.denominador);
  }
  
  void multiplicar(int multiplo) {
    this.numerador= this.numerador+(this.denominador*multiplo);
  }
  
  void sumar( Fraccion sumador) {
  
    if(this.denominador==sumador.denominador)
      this.numerador+=sumador.denominador;
    else {
      sumador.numerador*=this.denominador;
      this.numerador*=sumador.denominador;
      this.denominador*=sumador.denominador;
      this.numerador+=sumador.numerador;  
  
    }
  }
  
  void restar( Fraccion sumador) {
    
    if(this.denominador==sumador.denominador)
      this.numerador-=sumador.denominador;
    else {
      sumador.numerador*=this.denominador;
      this.numerador*=sumador.denominador;
      this.denominador*=sumador.denominador;
      this.numerador-=sumador.numerador;  
    }
  }
  
  void multiplicar (Fraccion frac) {
    this.numerador*=frac.numerador;
    this.denominador*=frac.denominador;
    
  }
  
  void simplificar () {
    int auxn=this.numerador;
    int auxd=this.denominador;
    for(int i=2; i<(auxn/2); i++) {
      
      for(;;) {
        if(auxn%i==0 && auxd%i==0) {
          this.denominador=this.denominador/i;
          this.numerador=this.numerador/i;
        }else {
          break;
        }
      }
      this.getValues();
      
    }
  }
}
