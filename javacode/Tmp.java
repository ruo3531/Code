class Tmp{
	public static void main(String[] args) {
		Dog dog = new Dog();
		System.out.print("call by method bark : ");
		dog.bark();
		System.out.print("call by method makesound in Dog : ");
		dog.makesound();
	}
}
class Animal {
	String name;
	String species;
	public void makesound() {
		System.out.println("Sound");
	}
}
class Dog extends Animal {
	public void makesound() {
		System.out.println("Woof!");
	}
	public void bark() {
		System.out.println("Woof!");
	}
} 