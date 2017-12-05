import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class solution2 {
    public static int validPasswords(String file) throws IOException {
        Scanner line = new Scanner(new File(file));
        int count = 0;
        while (line.hasNextLine()) {
            Scanner words = new Scanner(line.nextLine());
            Set<Map<Character, Integer>> seen = new HashSet<Map<Character, Integer>>();
            boolean good = true;
            while (words.hasNext()) {
                Map<Character, Integer> perm = new HashMap<Character, Integer>();
                for (Character c : words.next().toCharArray()) {
                    perm.put(c, perm.getOrDefault(c, 0) + 1);
                }
                
                if (!seen.add(perm)) {
                    good = false;
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


