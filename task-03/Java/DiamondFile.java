import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.io.FileWriter;
import java.util.Scanner;
public class DiamondFile {
    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        Scanner read = new Scanner(input);
        FileWriter output = new FileWriter("output.txt");
        int num = Integer.parseInt(read.nextLine());
        for(int i = 0; i <= num; i++) {
            for(int j = 0; j < num - i; j++) {
                output.write(" ");
            }
            for(int k = 0; k < i; k++) {
                output.write("* ");
            }
            output.write("\n");
        }
        for (int i = num-1; i >= 1; i--) {
            for (int j = num-i-1; j >= 0; j--) {
                output.write(" ");
            }
            for (int k = i - 1; k >= 0; k--) {
                output.write("* ");
            }
            output.write("\n");
        }
        output.close();
        read.close();
    }
}