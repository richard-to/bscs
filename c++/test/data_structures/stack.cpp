#include "gtest/gtest.h"
#include "data_structures/stack.h"

TEST(STACK, Basic)
{
    Stack stack = Stack();
    EXPECT_TRUE(stack.empty());
    stack.push(4);
    stack.push(5);
    EXPECT_FALSE(stack.empty());
    EXPECT_EQ(5, stack.pop());
    EXPECT_EQ(4, stack.peek());
    EXPECT_EQ(4, stack.pop());
    EXPECT_TRUE(stack.empty());
    stack.push(5);
    stack.push(12);
    EXPECT_FALSE(stack.empty());
    stack.clear();
    EXPECT_TRUE(stack.empty());
    stack.push(50);
}