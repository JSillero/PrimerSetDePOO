package ejerciciosobjetosJ;
/**
 * Programa prueba para circulo
 * @author d18sisaj
 *
 */

public class TestCirculo {

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    Circulo circulo= new Circulo(5.4);
 
    for(int i=0; i<27;i++) {
      circulo.incrementa(1.3);
    }
    System.out.println(circulo.ToString());
    
    for(int i=0; i<10;i++) {
      circulo.mengua(2.76);
    }
    
    System.out.println(circulo.ToString());
  
  
  
  
  
  
  }

}
