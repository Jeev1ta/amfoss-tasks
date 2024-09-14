import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.io.FileWriter;
public class FileRead {
    public static void main(String[] args) throws IOException {
        File input = new File("input.txt");
        Scanner read = new Scanner(input);
        FileWriter output = new FileWriter("output.txt");
        while (read.hasNextLine()) {
            String data = read.nextLine();
            output.write(data + System.lineSeparator());
        }
        read.close();
        output.close();
    }
}