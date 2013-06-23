#include "data_structures/queue.h"

QueueNode::QueueNode(int value)
{
    value_ = value;
    prev_ = 0;
}

QueueNode::~QueueNode()
{
    value_ = 0;
    prev_ = 0;
}

Queue::Queue()
{
    head_ = 0;
    tail_ = 0;
}

Queue::~Queue()
{
    clear();
}

bool Queue::empty()
{
    return head_ == 0;
}

void Queue::enqueue(int value)
{
    if (head_ == 0) {
        QueueNode* node = new QueueNode(value);
        head_ = node;
        tail_ = node;
    } else {
        QueueNode* node = new QueueNode(value);
        QueueNode* temp = tail_;
        tail_ = node;
        temp->prev_ = tail_;
    }
}

int Queue::dequeue()
{
    if (head_ == 0) {
        throw "Cannot dequeue on empty queue!";
    } else {
        QueueNode* temp = head_;
        int value = head_->value_;
        head_ = head_->prev_;
        if (temp == tail_) {
            tail_ = head_;
        }
        delete temp;
        return value;
    }
}

void Queue::clear()
{
    while (head_ != 0) {
        QueueNode* temp = head_;
        head_ = head_->prev_;
        delete temp;
    }
    tail_ = head_;
}