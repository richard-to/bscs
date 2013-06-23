#include "gtest/gtest.h"
#include "algorithms/fib.h"

TEST(FIB, Test_0)
{
    EXPECT_EQ(0, fib(0));
}

TEST(FIB, Test_1)
{
    EXPECT_EQ(1, fib(1));
}

TEST(FIB, Test_2)
{
    EXPECT_EQ(1, fib(2));
}

TEST(FIB, Test_Small)
{
    EXPECT_EQ(55, fib(10));
    EXPECT_EQ(377, fib(14));
    EXPECT_EQ(6765, fib(20));
}

TEST(FIB, Test_Large)
{
    EXPECT_EQ(832040, fib(30));
}