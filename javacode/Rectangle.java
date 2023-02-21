import java.util.Scanner;

public class Rectangle{
    double height = 1, width = 1;
    public Rectangle(){};
    public Rectangle(double w, double h){
        height = h;
        width = w;
    }
    public double getArea(){
        return height*width;
    }
    public double getPerimeter(){
        return (height+width)*2;
    }
    public static void main(String[] args){
        Rectangle rec1 = new Rectangle(4, 40);
        Rectangle rec2 = new Rectangle(3.5, 35.9);
        System.out.printf("rec1:\nwidth:%f\nheight:%f\ngetArea:%f\ngetPerimeter:%f\n",rec1.width, rec1.height, rec1.getArea(), rec1.getPerimeter());
        System.out.printf("rec2:\nwidth:%f\nheight:%f\ngetArea:%f\ngetPerimeter:%f\n",rec2.width, rec2.height, rec2.getArea(), rec2.getPerimeter());
    }
}

    
