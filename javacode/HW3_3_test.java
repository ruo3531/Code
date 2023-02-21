class HW3_3_test {
	public static void main(String[] args) {
		Car car = new Car("Audi", "A3");
		System.out.printf("Car:\ngetInfo(Audi, A3) : %s\n", car.getInfo());
		System.out.printf("getCapacity() : %d\n", car.getCapacity());

		Truck truck = new Truck("Ford", "F-150");
		System.out.printf("Truck:\ngetInfo(Ford, F-150) : %s\n", truck.getInfo());
		System.out.printf("getCapacity() : %d\n", truck.getCapacity());
	}
}

abstract class Vehicle {
	String make;
	String model;
	Vehicle(String a, String b) {
		make = a;
		model = b;
	}
	public abstract String getInfo();
}

class Truck extends Vehicle {
	Truck(String a, String b) {
		super(a, b);
	}
	public String getInfo() {
		return make + " " + model;
	}
	public int getCapacity() {
		return 6;
	}
}

class Car extends Vehicle {
	Car(String a, String b) {
		super(a, b);
	}
	public String getInfo() {
		return make + " " + model;
	}
	public int getCapacity() {
		return 5;
	}
}