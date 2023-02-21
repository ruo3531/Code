import java.util.Scanner;

public class HW5 {
    public static void main(String[] args){
        Scanner Input = new Scanner(System.in);
        System.out.print("Enter a letter: ");
        String check="AEIOU";
        char c = Input.next().charAt(0);
        if(!Character.isLetter(c))
            System.out.printf("%c is an invalid input", c);
        else{
            String tmp = String.valueOf(Character.toUpperCase(c));
            if(check.contains(tmp))
                System.out.printf("%c is a vawel", c);
            else
                System.out.printf("%c is a consonant", c);
        } 
            
    }
}
