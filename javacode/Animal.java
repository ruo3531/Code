class Animal {
	String name;
	String species;
	public void makesound(){
		System.out.printf("Sound\n");
	}
	public static void main(String[] args){
		Dog d = new Dog();
		System.out.printf("bark : ");
		d.bark();
		System.out.printf("makesound in Dog : ");
		d.makeSound();
	}
}
class Dog extends Animal {
	public void makeSound(){
		System.out.printf("Woof!\n");
	}
	public void bark(){
		System.out.printf("Woof!\n");
	}
} 