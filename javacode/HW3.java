import java.util.Scanner;

public class HW3 {
    public static void main(String[] args){
        Scanner Input = new Scanner(System.in);

        System.out.print("Enter a character: ");
        char c = Input.next().charAt(0);
        System.out.printf("The Unicode for the character %c is %d", c, (int)c);
    }
}
