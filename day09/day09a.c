#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char** argv) {
    FILE* file = fopen(argv[1], "r");
    unsigned score = 0;
    char c = 'c';
    unsigned level = 0; /* how deeply nested */
    unsigned rubbish = 0;
    while(c = fgetc(file), c != EOF) {
        switch (c) {
            case '!':
                fgetc(file);
                continue;
            case '>':
                rubbish = 0;
                continue;
            case '<':
                rubbish = 1;
                continue;
            case '{':
                if (!rubbish) {
                    ++level;
                }
                continue;
            case '}':
                if (!rubbish) {
                    score += level--;
                }
                continue;
            default:
                continue;
        }
    }
    fclose(file);
    printf("Score is %d\n", score);
    return 0;
}
