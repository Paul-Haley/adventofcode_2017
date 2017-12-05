#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {
    const int n = atoi(argv[1]);
    int i = 1; // value in spiral
    int l = 1; // length of side for current spiral level
    int s = 3; // side number going CCW from LHS
    int x = 0;
    int y = 0;
    while (i != n) {
        int d;
        if (i > n) { // Gone too far on current line
            int back = i - n;
            switch (--s) {
                case 0:
                    y -= back;
                    break;
                case 1:
                    x += back;
                    break;
                case 2:
                    y += back;
                    break;
                case 3:
                default:
                    x -= back;
                    break;
            }
            break;    
        }
        switch (s) {
            case 0:
                d = l - 2;
                y += d;
                break;
            case 1:
                d = l - 1;
                x -= d;
                break;
            case 2:
                d = l - 1;
                y -= d;
                break;
            case 3:
                d = l;
                x += l;
                l += 2;
                break;
        }
        i += d;
        ++s;
        s %= 4;
    }
    int moves = abs(x) + abs(y);
    printf("%d moves required from cell containing %d\n", moves, n);
    return 0;
}

