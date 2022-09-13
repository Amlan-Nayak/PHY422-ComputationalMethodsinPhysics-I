#include <stdio.h>

int main(void) {

    int value = 1;

    for (int i = 0; i < 37; i++) {

        printf("2^%d = %d\n", i, value);
        value = value * 2;
    }

    return 0;
}
