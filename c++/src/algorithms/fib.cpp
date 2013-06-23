#include "gtest/gtest.h"
#include "algorithms/fib.h"

long fib(long n)
{
    int startN = 3;
    int n1 = 1;
    int n2 = 1;
    int temp = 0;

    if (n == 0) {
        return 0;
    } else if (n == 1 or n == 2) {
        return 1;
    } else {
        int startN = 3;
        while (startN <= n) {
            temp = n1 + n2;
            n1 = n2;
            n2 = temp;
            ++startN;
        }
        return n2;
    }
}