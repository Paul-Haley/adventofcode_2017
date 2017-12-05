#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char** argv) {
    FILE* fd = fopen(argv[1], "r");
    unsigned cap = 512;
    unsigned cur = 0;
    int* numbers = malloc(cap * sizeof(int));
    char c [10];
    while (1) {
        if (fgets(c, 10, fd) == NULL) {
            numbers[cur] = atoi(c);
            break;
        }
        numbers[cur++] = atoi(c);
        if (cur == cap) {
            cap *= 2;
            int* tmp = malloc(cap * sizeof(int));
            memcpy(tmp, numbers, cur * sizeof(int));
            free(numbers);
            numbers = tmp;
        }
    }
    fclose(fd);

    int i = 0;
    int old = -1;
    unsigned jumps = 0;
    for(;;) {
        ++jumps;
        old = i;
        i += numbers[i];
        numbers[old] += numbers[old] >= 3 ? -1 : 1;
        if (i < 0 || i >= cur) {
            break;
        }
    }

    printf("Jumps = %d\n", jumps);
    return 0;
}
        
