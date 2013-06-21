#include "gtest/gtest.h"
#include "algorithms/insertion_sort.h"

TEST(INSERTION_SORT, Worst)
{
    int list[] = { 5, 4, 3, 2, 1 };
    int ex[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(list)/sizeof(list[0]);
    insertion_sort(list, size);
    for (int i = 0; i < size; i++) {
        EXPECT_EQ(ex[i], list[i]);
    }
}

TEST(INSERTION_SORT, Best)
{
    int list[] = { 1, 2, 3, 4, 5 };
    int ex[] = { 1, 2, 3, 4, 5 };
    int size = sizeof(list)/sizeof(list[0]);
    insertion_sort(list, size);
    for (int i = 0; i < size; i++) {
        EXPECT_EQ(ex[i], list[i]);
    }
}

TEST(INSERTION_SORT, Othe)
{
    int list[] = { 20, -1, -2, -1, 0, 20, 12 };
    int ex[] = { -2, -1, -1, 0, 12, 20, 20 };
    int size = sizeof(list)/sizeof(list[0]);
    insertion_sort(list, size);
    for (int i = 0; i < size; i++) {
        EXPECT_EQ(ex[i], list[i]);
    }
}