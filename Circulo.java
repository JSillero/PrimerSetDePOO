package ejerciciosobjetosJ;
import javax.swing.*;
public class Circulo {
  double radio;
  
  Circulo(double r){
    this.radio=r;
    if(this.radio<=0) {
      this.radio=0;
      JOptionPane.showInternalMessageDialog(null, "Soy un misero punto sin area");
    }
  }
  
  void incrementa( double inc) {
    this.radio+=inc;
    
  }
  
  void mengua( double men) {
    this.radio-=men;
    if(this.radio<=0) {
      this.radio=0;
      JOptionPane.showInternalMessageDialog(null, "Soy un misero punto sin area");
      
    }
  }
  double area() {
    double area=this.radio*this.radio*Math.PI;
    return area;
  }
  String ToString() {
    return ("Soy un circulo de: "+ Double.toString(this.radio) +" radio y "+Double.toString(this.area())+" area.");
    
  }
}


