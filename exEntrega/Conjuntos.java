import java.util.ArrayList;
public class Conjuntos {

  public static void main(String[] args) {
    operationG();
    operationH();
    operationI();
    operationJ();
    operationL();
    operationHH();
  }

  static void operationG() {
    System.out.println("Operação G");
    for(double i = 0.01; i < 1; i+= 0.01){
      System.out.println(Math.round(i * 100.0)/100.0);
    }
  }
  
  static void operationH(){
    System.out.println("Operação H");
    for(int i = 97; i < 123; i++){
      System.out.println((char)i);
    }
  }

  static void operationI(){
    System.out.println("Operação I");
    boolean a = true;
    System.out.println(a);
    System.out.println(!a);
  }
  
  static void operationJ(){
    System.out.println("Operação J");
    for(int i = 0; i < 128; i++){
      System.out.println(getBinary(i));
    }
  }
  
  static void operationL(){
    System.out.println("Operação J");
    for (int i = 1; i<= (360); i++){
      System.out.println(i);
    }
  }

  static void operationHH(){
    System.out.println("Operação HH");
    for(int i = 97; i < 123; i++){
      if (i != 97 && i != 101 && i != 105 && i != 111 && i != 117){
        System.out.println((char)i);
      }
    }
  }

  static String getBinary(int dec){

    ArrayList<Integer> binary = new ArrayList<Integer>();
    char[] try1;
    int binInt;
    String aux, bin;


    aux = "";
    bin = "";

    while (dec > 0) {
      binInt = dec % 2;
      dec = dec / 2;
      binary.add(binInt);
    }

    for (Integer i : binary) {
      aux += i;
    }

    try1 = aux.toCharArray();

    for (int i = try1.length - 1; i >= 0; i--)
      bin += try1[i];

    return (bin);


  }

}