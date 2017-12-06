import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Day06b {

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File(args[0]);
        Scanner line = new Scanner(file);
        Scanner scanner = new Scanner(line.nextLine());
        line.close();
        List<Integer> memory = new ArrayList<Integer>();
        scanner.useDelimiter("\t");
        while(scanner.hasNext()) {
            memory.add(Integer.parseInt(scanner.next()));
        }
        scanner.close();
        System.out.println("Cycles = " + cycles(memory, true));
    }
    
    public static int cycles(List<Integer> memory, boolean firstRun) {
        Set<List<Integer>> seen = new HashSet<List<Integer>>();
        int iterations = 0;
        while(true) {
            if (!seen.add(memory)) {
                if (firstRun) {
                    return cycles(memory, false);
                } else {
                    return iterations;
                }
            }
            ++iterations;
            
            List<Integer> next = new ArrayList<Integer>(memory.size());
            next.addAll(memory);
            memory = next;
            
            int max = findMax(memory);
            int distribute = memory.get(max); // distributing max value over memory
            memory.set(max, 0);
            int j = (max + 1) % memory.size();
            for(; distribute > 0; --distribute) {
                memory.set(j, memory.get(j) + 1);
                j = (j + 1) % memory.size();
            }
        }
    }
    
    public static int findMax(List<Integer> memory) {
        int max = 0;
        for(int i = 1; i < memory.size(); ++i) {
            if (memory.get(i) > memory.get(max)) {
                max = i;
            }
        }
        return max;
    }

}
