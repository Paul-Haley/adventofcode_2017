#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char** argv) {
    uint64_t A = 883, B = 879, Afactor = 16807, Bfactor = 48271, div = 2147483647;
    unsigned i, matches = 0;
    for(i = 0; i < 40000000; ++i) {
    //for(i = 0; i < 5; ++i) {
        A *= Afactor;
        A %= div;
        B *= Bfactor;
        B %= div;
        (A & 0x0000FFFF) != (B & 0x0000FFFF) ? : ++matches ;
    }
    printf("%u\n", matches);
}
    


