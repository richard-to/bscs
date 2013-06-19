#include "gtest/gtest.h"
#include "algorithms/binary_search.h"

TEST(BINARY_SEARCH, Found)
{
    int list[] = { -10, -2, 0, 4, 20, 21, 22 };
    int size = sizeof(list) / sizeof(list[0]);
    EXPECT_TRUE(binary_search(4, list, 0, size));
    EXPECT_TRUE(binary_search(22, list, 0, size));
    EXPECT_TRUE(binary_search(-10, list, 0, size));
}

TEST(BINARY_SEARCH, NotFound)
{
    int list[] = { -10, -2, 0, 4, 20, 21, 22 };
    int size = sizeof(list) / sizeof(list[0]);
    EXPECT_FALSE(binary_search(5, list, 0, size));
    EXPECT_FALSE(binary_search(223, list, 0, size));
    EXPECT_FALSE(binary_search(-1, list, 0, size));
}