import java.util.Scanner;

public class HW4 {
    public static void main(String[] args){
        Scanner Input = new Scanner(System.in);
        String Str = "0123456789ABCDEF";
        System.out.print("Enter a decimal value (0 to 15): ");
        int n = Input.nextInt();
        if(n > 15)
            System.out.printf("%d is an invalid input", n);
        else 
            System.out.printf("The hex value is %s", Str.charAt(n));
    }
}
