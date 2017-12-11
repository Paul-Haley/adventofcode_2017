#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <ctype.h>

void reverse(unsigned cursor, unsigned len, unsigned* list, unsigned size) {
    unsigned i = 0;
    for(; i < len/2; ++i) {
        unsigned tmp = list[(cursor + i)%size];
        list[(cursor+i)%size] = list[((cursor + len) - (i + 1))%size];
        list[((cursor + len) - (i + 1))%size] = tmp;
    }
}

int main(int argc, char** argv) {
    const unsigned SIZE = 256;
    const unsigned INPUT_SIZE = 16;
    unsigned* list = (unsigned*) malloc(sizeof(unsigned) * SIZE);
    int i = 0;
    for(; i < SIZE; ++i) { // populate list 0-255
        list[i] = i;
    }

    unsigned* lengths = (unsigned*) malloc(sizeof(unsigned) * INPUT_SIZE);
    FILE* file = fopen(argv[1], "r");
    char number[4], c;
    i = 0;
    unsigned j = 0; // index into lengths
    while(c = fgetc(file), c != EOF) { // reading lengths given (input)
        if(isdigit(c)) {
            number[i++] = c;
        } else {
            number[i] = '\0';
            lengths[j++] = (unsigned) strtol(number, NULL, 10);
            i = 0;
        }
    }
    
    unsigned cursor = 0;
    unsigned l = 0; // length index
    unsigned skipSize = 0;
    for(; l < INPUT_SIZE; ++l) { // hashing
        reverse(cursor, lengths[l], list, SIZE);
        cursor += lengths[l] + skipSize++;
    }
    printf("%d x %d = %d\n", list[0], list[1], list[0] * list[1]);

    // clean up
    fclose(file);
    free(lengths);
    free(list);
    return 0;
}
