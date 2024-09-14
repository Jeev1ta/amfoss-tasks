import java.util.Scanner;
public class Diamond {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int num = myObj.nextInt();
        for(int i = 0; i <= num; i++) {
            for(int j = 0; j < num - i; j++) {
                System.out.print(" ");
            }
            for(int k = 0; k < i; k++) {
                System.out.print("* ");
            }
            System.out.print("\n");
        }
        for (int i = num-1; i >= 1; i--) {
            for (int j = num-i-1; j >= 0; j--) {
                System.out.print(" ");
            }
            for (int k = i - 1; k >= 0; k--) {
                System.out.print("* ");
            }
            System.out.print("\n");
        }
    }
}