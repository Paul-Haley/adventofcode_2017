import java.util.HashMap;
import java.util.Map;

public class SpiralSum {    
    public static int firstLarger(int goal) {
        Map<Point, Integer> grid = new HashMap<Point, Integer>();
        int d = 0; // 0 means upwards, number increases CCW mod 4
        int l = 3;
        int rem = 2; // remainder left for line
        int sum = 1;
        Point current = new Point(1, 0);
        grid.put(new Point(0,0), 1);
        
        while (sum < goal) {
            //System.out.println(current);
            sum = getSurrounding(grid, current);
            grid.put(current, sum);
            --rem; 
            if (rem == 0) { // end of line
                d = (d + 1) % 4; // change direction
                rem = l - 1;
                //System.out.println("cd, d=" +d+", rem=" +rem + ", l=" + l);
            }
            
            int x = current.x;
            int y = current.y;
            switch (d) { // changing grid reference for next run
                case 0: // need to increase length
                    ++y;
                    l += rem == l-1 ? 1 : 0;
                    break;
                case 1: 
                    --x;
                    break;
                case 2: // need to increase length
                    --y;
                    l += rem == l-1 ? 1 : 0;
                    break;
                case 3:
                default:
                    ++x;
                    break;
            }
            current = new Point(x, y);
        }
        return sum;
    }
    
    /**
     * Brute force search for all surrounding values of a point
     * @param x
     * @param y
     * @return sum of all surrounding points that exist
     */
    private static int getSurrounding(Map<Point, Integer> grid, Point current) {
        int surrounding = 0;
        for (int i = -1; i <= 1; ++i) {
            for (int j = -1; j <= 1; ++j) {
                Integer value = grid.get(new Point(current.x + i, current.y + j));
                surrounding += (value != null) ? value : 0;
            }
        }
        return surrounding;
    }
    
    public static void main(String[] args) {
        System.out.println(firstLarger(Integer.parseInt(args[0])));
    }
}
