import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Day23a {
    static Map<Character, Long> initialiseRegisters() {
        Map<Character, Long> reg = new HashMap<Character, Long>();
        for (char c = 'a'; c <= 'h'; ++c) {
            reg.put(c, 0l);
        }
        return reg;
    }
    
    static List<String[]> readInstructions(String file) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(file));
        List<String[]> instructions = new ArrayList<String[]>();
        while (scanner.hasNextLine()) {
            instructions.add(scanner.nextLine().split(" "));
        }
        scanner.close();
        return instructions;
    }
    
    static long firstRecover(List<String[]> instructions) throws FileNotFoundException {
        Map<Character, Long> reg = initialiseRegisters();
        long muls = 0;
        int i = 0; // instruction number
        while (0 <= i && i < instructions.size()) {
            String[] parts = instructions.get(i);
            switch (parts[0]) {
                case "set":
                    reg.put(parts[1].charAt(0), getValue(parts[2], reg));
                    break;
                case "sub":
                    char a = parts[1].charAt(0);
                    reg.put(a, reg.get(a) - getValue(parts[2], reg));
                    break;
                case "mul":
                    ++muls;
                    char mu = parts[1].charAt(0);
                    reg.put(mu, reg.get(mu) * getValue(parts[2], reg));
                    break;
                case "jnz": 
                    if (getValue(parts[1], reg) != 0) {
                        i += getValue(parts[2], reg);
                        continue;
                    }
            }
            ++i;
        }
        return muls;
    }
    
    /**
     * Part could be number or register, figure out what it is and return the correct value
     * @param regOrValue String of number or register
     * @param reg registers
     * @return value trying to be described
     */
    public static long getValue(String regOrValue, Map<Character, Long> reg) {
        return Character.isAlphabetic(regOrValue.charAt(0)) ? reg.get(regOrValue.charAt(0)) : Long.parseLong(regOrValue);
    }
    
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println(firstRecover(readInstructions(args[0])));
    }

}
