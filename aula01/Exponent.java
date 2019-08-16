import java.util.Scanner;

public class Exponent {

	static void operation(double base, double expo) {
		int cont = 0;
		double tempBase = base;
		if (expo == 0) {
			System.out.println(base + " to the power of " + expo + " = " + 1);
		} else {
		cont = 1;
		while (cont < expo) {
			tempBase = tempBase * base;
			cont++;
		}
			System.out.println(base + " to the power of " + expo + " = " + tempBase);
		}
	}

	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		double base, exponent;

		System.out.println("What is the base of the operation?");
		base = keyboard.nextDouble();
		System.out.println("What is the exponent of the operation?");
		exponent = keyboard.nextDouble();

		operation(base, exponent);

		keyboard.close();

	}

}