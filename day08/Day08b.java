import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Day08b {
    
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("highest value ever was " + findHighest(args[0]));
    }

    private static int findHighest(String file) throws FileNotFoundException {
        Map<String, Integer> reg = new TreeMap<String, Integer>();
        Scanner scanner = new Scanner(new File(file));
        int highestValue = 0;
        while(scanner.hasNextLine()) {
            String[] parts = scanner.nextLine().split(" ");
            if(isTrue(parts, reg)) {
                int change = Integer.parseInt(parts[2]);
                int newValue = reg.getOrDefault(parts[0], 0) + (parts[1].equals("inc") ? change : -change);
                if(newValue > highestValue) {
                    highestValue = newValue;
                }
                reg.put(parts[0], newValue);
            }
        }
        scanner.close();
        return highestValue;
    }


    private static boolean isTrue(String[] parts, Map<String, Integer> reg) {
        int val = reg.getOrDefault(parts[4], 0);
        int com = Integer.parseInt(parts[6]);
        switch (parts[5]) {
            case ">=":
                return val >= com;
            case ">":
                return val > com;
            case "<=":
                return val <= com;
            case "<":
                return val < com;
            case "==":
                return val == com;
            case "!=":
                return val != com;
            default:
                return false;
        }
    }
}
