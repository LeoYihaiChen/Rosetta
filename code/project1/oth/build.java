public class BinaryToDecimal {
    public static void main(String[] args) {
        String binaryNumber = "1010";
        
        int decimalNumber = Integer.parseInt(binaryNumber, 2); 
        
        System.out.println("Binary number: " + binaryNumber);
        System.out.println("Decimal number: " + decimalNumber);
    }
}