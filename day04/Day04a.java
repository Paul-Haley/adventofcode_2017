import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Day04a {
    public static int validPasswords(String file) throws IOException {
        Scanner line = new Scanner(new File(file));
        int count = 0;
        while (line.hasNextLine()) {
            Scanner words = new Scanner(line.nextLine());
            Set<String> seen = new HashSet<String>();
            boolean good = true;
            while (words.hasNext()) {
                if (!seen.add(words.next())) {
                    good = false;
                    break;
                }
            }
            words.close();
            count += good ? 1 : 0;
        }       
        line.close();
        return count;
    }
    
    public static void main(String[] args) throws IOException {
        System.out.println(validPasswords(args[0]));
    }
}


