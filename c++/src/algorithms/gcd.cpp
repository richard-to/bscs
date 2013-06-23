#include "algorithms/gcd.h"

int gcd(int a, int b)
{
    int remainder = a % b;
    if (remainder == 0) {
        return b;
    } else {
        return gcd(b, remainder);
    }
}