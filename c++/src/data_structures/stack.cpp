#include "data_structures/stack.h"

StackNode::StackNode(int value)
{
    value_ = value;
    next_ = 0;
}

StackNode::~StackNode()
{
    value_ = 0;
    next_ = 0;
}

Stack::Stack()
{
    head_ = 0;
}

Stack::~Stack()
{
    clear();
}

bool Stack::empty()
{
    return head_ == 0;
}

void Stack::push(int value)
{
    if (head_ == 0) {
        head_ = new StackNode(value);
    } else {
        StackNode* temp = head_;
        head_ = new StackNode(value);
        head_->next_ = temp;
    }
}

int Stack::peek()
{
    if (head_ == 0) {
        throw "Can't peek on empty stack!";
    } else {
        return head_->value_;
    }
}

int Stack::pop()
{
    if (head_ == 0) {
        throw "Can't pop on empty stack!";
    } else {
        StackNode* temp = head_;
        int value = head_->value_;
        head_ = head_->next_;
        delete temp;
        return value;
    }
}

void Stack::clear()
{
    while (head_ != 0) {
        StackNode* temp = head_;
        head_ = head_->next_;
        delete temp;
    }
}