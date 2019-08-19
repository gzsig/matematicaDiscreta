import java.util.Scanner;

public class Range {

	static void operation(int xValue, String operation) {

		if (operation.contains("<")) {
			operation = operation.replaceAll("\\D+", "");
			int result = Integer.parseInt(operation);
			int cont = 0;
			while (xValue < result) {
				System.out.println(xValue);
				xValue++;
				cont++;
			}
			System.out.println("there are " + cont + " numbers" );
		} else if (operation.contains(">")) {
			operation = operation.replaceAll("\\D+", "");
			int result = Integer.parseInt(operation);
			int cont = 0;
			while (xValue > result) {
				System.out.println(xValue);
				xValue--;
				cont++;
			}
			System.out.println("there are " + cont + " numbers" );
		}

	}

	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);

		int xValue;
		String secondOp;

		System.out.println("What is the value of X?");
		xValue = keyboard.nextInt();
		System.out.println("What is the equation?");
		secondOp = keyboard.next();

		operation(xValue, secondOp);

		keyboard.close();

	}

}