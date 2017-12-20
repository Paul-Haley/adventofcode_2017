import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;

public class Day18b {
    public static final int PROGRAMS = 2;
    
    static Map<Character, Long> initialiseRegisters() {
        Map<Character, Long> reg = new HashMap<Character, Long>();
        for (char c = 'a'; c <= 'z'; ++c) {
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
    
    static long firstRecover(List<String[]> instructions) {
        List<Map<Character, Long>> reg = new ArrayList<Map<Character, Long>>();
        List<Queue<Long>> data = new ArrayList<Queue<Long>>();
        int[] step = new int[2];
        boolean[] running = new boolean[2];
        for(int i = 0; i < 2; ++i) {
            step[i] = 0;
            running[i] = true;
            reg.add(initialiseRegisters());
            reg.get(i).put('p', (long) i);
            data.add(new LinkedList<Long>());
        }
        
        long id1Send = 0;
        int current = 0;
        while (!isDeadlock(running)) {
            current = (current + 1) % PROGRAMS;
            String[] parts = instructions.get(step[current]);
            switch (parts[0]) {
                case "snd":
                    id1Send += current == 1 ? 1 : 0; // program 1 send, increment
                    data.get((current + 1) % PROGRAMS).add(getValue(parts[1], reg.get(current)));
                    break;
                case "set":
                    reg.get(current).put(parts[1].charAt(0), getValue(parts[2], reg.get(current)));
                    break;
                case "add":
                    char a = parts[1].charAt(0);
                    reg.get(current).put(a, reg.get(current).get(a) + getValue(parts[2], reg.get(current)));
                    break;
                case "mul":
                    char mu = parts[1].charAt(0);
                    reg.get(current).put(mu, reg.get(current).get(mu) * getValue(parts[2], reg.get(current)));
                    break;
                case "mod":
                    char mo = parts[1].charAt(0);
                    reg.get(current).put(mo, reg.get(current).get(mo) % getValue(parts[2], reg.get(current)));
                    break;
                case "rcv":
                    if (data.get(current).isEmpty()) {
                        running[current] = false;
                        continue; // let someone else run
                    } else {
                        running[current] = true;
                        reg.get(current).put(parts[1].charAt(0), data.get(current).remove());
                        break;
                    }
                case "jgz": 
                    if (getValue(parts[1], reg.get(current)) > 0) {
                        step[current] += getValue(parts[2], reg.get(current));
                        continue;
                    }
            }
            ++step[current];
        }
        return id1Send;
    }
    
    /**
     * @param running list of booleans for programms running (true if running)
     * @return true if deadlock, false otherwise
     */
    private static boolean isDeadlock(boolean[] running) {
        for(boolean b : running) {
            if (b) {
                return false;
            }
        }
        return true;
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
