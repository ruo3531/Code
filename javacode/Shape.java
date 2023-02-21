class Shape {
	String name;
	int sides;
	Shape(String Name, int s){
		name = Name;
		sides = s;
	}
	public void getInfo(){
		System.out.printf("name: %s\nsides: %d\n", name, sides);
	}
	public static void main(String[] args){
		Triangle tmp = new Triangle();
		System.out.print("getInfo():\n");
		tmp.getInfo();
		System.out.print("\ngetArea(3, 4):\n");
		tmp.getArea(3, 4);
	}
}

class Triangle extends Shape {
	Triangle(){
		super("triangle", 3);
	}
	Triangle(String a, int b){
		super(a, b);
	}
	public void getInfo(){
		System.out.printf("name: %s\nsides: %d\n", "triangle", 3);
	}
	public void getArea(double base, double height){
		System.out.printf("the area of triangle is : %.1f\n" , base * height * 0.5);
	}
}