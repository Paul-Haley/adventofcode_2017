import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Day08a {
    
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("highest value is " + findHighest(args[0]));
    }

    private static int findHighest(String file) throws FileNotFoundException {
        Map<String, Integer> reg = new TreeMap<String, Integer>();
        Scanner scanner = new Scanner(new File(file));
        while(scanner.hasNextLine()) {
            String[] parts = scanner.nextLine().split(" ");
            if(isTrue(parts, reg)) {
                int change = Integer.parseInt(parts[2]);
                reg.put(parts[0], reg.getOrDefault(parts[0], 0) + (parts[1].equals("inc") ? change : -change));
            }
        }
        scanner.close();
        return getLargest(reg);
    }

    /**
     * @param reg
     * @return
     */
    private static int getLargest(Map<String, Integer> reg) {
        int highest = 0;
        for(Integer i : reg.values()) {
            if (i > highest) {
                highest = i;
            }
        }
        return highest;
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
