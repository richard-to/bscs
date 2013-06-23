#include "gtest/gtest.h"
#include "algorithms/gcd.h"

TEST(GCD, Basic)
{
    EXPECT_EQ(2, gcd(34, 20));
}

TEST(GCD, SmallerA)
{
    EXPECT_EQ(2, gcd(20, 34));
    EXPECT_EQ(5, gcd(5, 420));
}

TEST(GCD, Negative)
{
    EXPECT_EQ(2, gcd(-20, 34));
    EXPECT_EQ(5, gcd(5, -420));
}

TEST(GCD, gcd1)
{
    EXPECT_EQ(1, gcd(3242,-4233));
}