#include <stdio.h>
#include <stdlib.h>

main() {
    long a = 1l, b,c,d,e,f,g,h;
    b = c = d = e = f = g = h = 0l;

    l1: b = 67l;
    l2: c = b;
    l3: if (a != 0l) goto l5;
    l4: goto l9;
    l5: b *= 100l;
    l6: b += 100000l;
    l7: c = b;
    l8: c += 17000l;
    l9: f = 1l;
    l10: d = 2l;
    l11: e = 2l;
    l12: g = d;
    l13: g *= e;
    l14: g -= b;
    l15: if (g != 0l) goto l17;
    l16: f = 0l;
    l17: ++e;
    l18: g = e;
    l19: g -= b;
    l20: if (g != 0l) goto l12;
    l21: ++d;
    l22: g = d;
    l23: g -= b;
    l24: if (g != 0) goto l11;
    l25: if (f != 0) goto l27;
    l26: ++h;
    l27: g = b;
    l28: g -= c;
    l29: if (g != 0) goto l31;
    l30: goto end;
    l31: b += 17;
    l32: goto l9;
    end: printf("h=%ld\n", h);
    return 0;
}
