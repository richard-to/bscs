#include "algorithms/binary_search.h"

bool binary_search(int find, int list[], int start, int length)
{
    int mid = (length / 2) + start;
    if (length == 1) {
        return find == list[start];
    } else if (find == list[mid]) {
        return true;
    } else if (find > list[mid]) {
        return binary_search(find, list, mid, (length + start) - mid);
    } else if (find < list[mid]) {
        return binary_search(find, list, start, mid - start);
    }
}