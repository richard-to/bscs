#include "algorithms/insertion_sort.h"

void insertion_sort(int list[], int size)
{
    int value = 0;
    int pos = 0;
    for (int i = 1; i < size; ++i) {
        value = list[i];
        pos = i - 1;
        while (pos >= 0 && value < list[pos]) {
            list[pos + 1] = list[pos];
            --pos;
        }
        list[pos + 1] = value;
    }
}